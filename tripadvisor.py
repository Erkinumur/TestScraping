import json

import requests
from fake_useragent import UserAgent
from parsel import Selector

from models import ReviewData

url = 'https://www.tripadvisor.com/Restaurant_Review-g295424-d10336417-' \
      'Reviews-Couqley_French_Bistro_Dubai-Dubai_Emirate_of_Dubai.html'
base_url = 'https://www.tripadvisor.com'
profile_url = base_url + '/Profile/'

ua = UserAgent()
headers = {
    'authority': 'www.google.com',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                  '(KHTML, like Gecko)   Chrome/102.0.0.0 Safari/537.36'}
proxies = {
    'http': '5.189.151.227:24031',
    'https': '5.189.151.227:24031'
}

response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
selector = Selector(response.text)


def parse_reviews(selector):
    review_containers = selector.xpath('//div[@class="review-container"]')

    reviews = []

    for div in review_containers:
        author_img = div.xpath('.//div[contains(@class, "ui_avatar")]/img/@data-lazyurl').get()
        author_name = div.xpath('.//div[contains(@class, "info_text")]/div/text()').get()
        author_url = profile_url + author_name

        raiting = div.xpath('.//span[contains(@class, "ui_bubble_rating")]/@class')
        raiting = int(raiting.get()[-2])

        raiting_date = div.xpath('.//span[@class="ratingDate"]/@title').get()

        review_title = div.xpath('.//span[@class="noQuotes"]/text()').get()

        review_text = div.xpath('.//p[@class="partial_entry"]')
        additional_text = review_text.xpath('span/text()').get()
        review_text = review_text.xpath('text()').get()
        if additional_text:
            review_text += additional_text

        reviews.append(ReviewData(
            author_name=author_name,
            author_url=author_url,
            author_photo_url=author_img,
            raiting=raiting,
            text=f'{review_title}\n{review_text}',
            created_at=raiting_date
        ))

    return reviews


if __name__ == '__main__':
    print(response.status_code)
    reviews = parse_reviews(selector)

    with open('tripadvisor.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps([i.__dict__ for i in reviews], ensure_ascii=False))

    print(len(reviews))
