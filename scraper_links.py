class ScraperLinks(AsyncScraper):
    BASE_URL = 'https://www.google.com'
    SEARCH_URL = 'https://www.google.com/search'

    NEXT_PAGE_XPATH = '//div[@role="navigation"][table]//td[a[span[text()="Next"]]]/a/@href'

    def __init__(self, prefetch_count: int = PREFETCH_COUNT,
                 service_name: str = SERVICE_NAME_LINKS):
        super().__init__(prefetch_count, service_name)
        self.fetcher_client = AsyncFetcherClient(self)
        self.publisher = Publisher()

    async def send_request(self, message: AsyncAcceleratorIncomingMessage, url: str, callback: str,
                           method: str = 'GET', meta: dict = None, data: dict = None,
                           params: dict = None):
        r = Request(method=method, url=url, headers=DEFAULT_HEADERS_GOOGLE,
                    proxies=DEFAULT_PROXIES, max_retries=DEFAULT_RETRIES,
                    allowed_http_codes=[200], params=params, timeout=DEFAULT_TIMEOUT)
        if data:
            r.data = data

        await self.fetcher_client.send(FetcherTaskMessageBody(r, callback=callback, meta=meta),
                                       message)

    async def start(self, message: AsyncAcceleratorIncomingMessage, message_body: dict):
        response = FetcherResponse.from_dict(message_body)
        meta = response.request.meta
        sites = meta.get('sites')
        limit = meta.get('limit', 10)
        offset = meta.get('offset', 0)

        companies = db.get_companies_search_info(limit=limit, offset=offset)
        print(len(companies))

        for company in companies:
            search_query = f'{company.name}+{company.city}+{company.state}+{company.street}+' \
                           f'{company.zip}'.replace(' ', '+')
            search_query = search_query.replace('&', '%26')

            meta = {
                'sites': sites,
                'search_query': search_query
            }
            await self.send_request(message, url=self.SEARCH_URL, callback='extract_links',
                                    method='GET', meta=meta, params={'q': search_query})

    async def extract_links(self, message: AsyncAcceleratorIncomingMessage, message_body: dict):
        response = FetcherResponse.from_dict(message_body)
        content = response.response.text()
        tree = Selector(text=content)
        meta = response.request.meta

        sites = meta.get('sites')
        links = {}

        for key, value in sites.items():
            link = tree.xpath(f'//a[contains(@href, "{value}")]/@href').get()
            if link:
                links[key] = link

        for key, value in links.items():
            task = {
                'request': {
                    'callback': 'start',
                    'url': value
                }
            }

            self.publisher(task, key)
            sites.pop(key)

        if sites:
            next_page = tree.xpath(self.NEXT_PAGE_XPATH).get()
            if next_page:
                url = self.BASE_URL + next_page
                await self.send_request(message, url=url, callback='extract_links',
                                        method='GET', meta={'sites': sites})
            else:
                companies = []
                for site in sites.values():
                    source = db.get_or_create_source(Source(name=site.split('.')[0]))
                    company = NotFoundCompany(
                        url=f'{self.SEARCH_URL}?q={meta.get("search_query")}',
                        search_query=meta.get("search_query"),
                        source_id=source.id
                    )
                    companies.append(company)

                db.save_objects(companies)