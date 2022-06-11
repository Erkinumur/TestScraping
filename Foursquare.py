import requests
from fake_useragent import UserAgent
from parsel import Selector

base_url = 'https://foursquare.com'
url = 'https://ru.foursquare.com/v/friendlys/4b632609f964a5207a662ae3'

ua = UserAgent()
headers = {'User-agent': ua.chrome}
response = requests.get(url, headers=headers)
selector = Selector(response.text)


def parse_reviews(selector):

    li_list = selector.xpath('//ul[@id="tipsList"]/li')

    reviews = []

    for li in li_list:
        author_name = li.xpath('.//span[@class="userName"]/a/text()').get()

        author_url = base_url + li.xpath('div[@class="authorImage"]/a/@href').get()

        author_image = li.xpath('div[@class="authorImage"]//img[contains(@class, "avatar")]')
        author_image = author_image.attrib.get('src')

        review_date = li.xpath('.//span[@class="tipDate"]/text()').get()

        review_text_div = li.xpath('.//div[@class="tipText"]')
        div_texts = review_text_div.xpath('text()')
        span_texts = review_text_div.xpath('span/text()')
        review_text = ''

        for i in range(len(span_texts)):
            review_text += div_texts.pop(0).get()
            review_text += span_texts.pop(0).get()

        if div_texts:
            review_text += div_texts.pop(0).get()

        reviews.append({
            'author_name': author_name,
            'author_url': author_url,
            'author_image': author_image,
            'review_date': review_date,
            'review_text': review_text
            })

    return reviews
