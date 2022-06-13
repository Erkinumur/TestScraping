import json
from time import sleep

import requests
from fake_useragent import UserAgent
from parsel import Selector

from TestScraping.models import ReviewData

url = 'https://www.google.com/search?q=ace+florist+in+syosset+ny+11791'
review_sort_url = 'https://www.google.com/async/reviewSort'

ua = UserAgent()

headers = {
    'authority': 'www.google.com',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,' \
    #            'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                  'like Gecko)   Chrome/102.0.0.0 Safari/537.36'
}

proxies = {
    'http': '5.189.151.227:24031',
    'https': '5.189.151.227:24031'
}
params = {'async': 'feature_id:0x89c28248873aae9f%3A0x9062074cae10c10f,review_source:All%20reviews,sort_by:qualityScore,is_owner:false,filter_text:,associated_topic:,async_id_prefix:,_pms:s,_fmt:pc'}

response = requests.get(url, headers=headers)
selector = Selector(response.text)


def get_next_page(selector):
    next_page_token = selector.xpath('//div[@data-next-page-token]/@data-next-page-token').get()
    print(next_page_token)
    if not next_page_token:
        raise Exception('Страниц больше нет')

    next_page_token = next_page_token.strip('=')
    async_param = params.get('async') + f',next_page_token:{next_page_token}'
    res = response = requests.get(
        review_sort_url, headers=headers,
        params={'async': async_param}, proxies=proxies
    )

    if res.status_code != 200:
        raise Exception(f'Bad request: {res.status_code}')

    return Selector(res.text)


def parse_reviews(selector):
    divs = selector.xpath('//div[@data-next-page-token]/div')
    reviews = []

    for div in divs:
        container = div.xpath('div[g-dropdown-menu]')

        author_name = container.xpath('div[div/a]//a/text()').get().strip()
        author_url = container.xpath('div[div/a]//a/@href').get()
        author_photo_url = div.xpath('a/img/@src').get()

        text = container.xpath('.//span[@data-expanded-section]/text()')

        if not text:
            text = container.xpath('.//span[@class="review-full-text"]/text()')
            if text:
                text = text[2]

        text = text.get()

        raiting = container.xpath('.//g-review-stars/span/@aria-label').get()
        raiting = raiting[:-1].replace(',', '.').split()
        raiting = [i for i in raiting if '.' in i][0]
        raiting = float(raiting)

        reviews.append(ReviewData(
            author_name=author_name,
            author_photo_url=author_photo_url,
            text=text,
            author_url=author_url,
            raiting=raiting
        ))

    return reviews


def parse_reviews_sort_payload(selector):
    global params
    payload = selector.xpath('//a[@data-fid]')[0].attrib
    params = {
        'async': f'feature_id:{payload.get("data-fid")},review_source:All%20reviews,'
                 f'sort_by:{payload.get("data-sort_by")},'
                 f'is_owner:{payload.get("data-is_owner")},filter_text:,associated_topic:,'
                 f'async_id_prefix:,_pms:s,'
                 f'_fmt:pc'
    }
    res = requests.get(review_sort_url, headers=headers, params=params)
    print(res.status_code)
    return res


def parse():
    reviews_response = parse_reviews_sort_payload(selector)
    _selector = Selector(reviews_response.text)

    reviews = []

    while True:
        print('parse')
        reviews.extend(parse_reviews(_selector))

        try:
            _selector = get_next_page(_selector)
        except Exception as e:
            print(e)
            break

        sleep(1)

    return reviews


if __name__ == '__main__':
    reviews = parse()

    with open('google.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps([i.__dict__ for i in reviews], ensure_ascii=False))

    print(len(reviews))

