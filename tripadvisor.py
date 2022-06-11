import requests
from fake_useragent import UserAgent
from parsel import Selector

url = 'https://www.tripadvisor.com/Restaurant_Review-g295424-d10336417-' \
      'Reviews-Couqley_French_Bistro_Dubai-Dubai_Emirate_of_Dubai.html'

ua = UserAgent()
headers = {'User-agent': ua.chrome}
response = requests.get(url, headers=headers)
selector = Selector(response.text)


def parse_reviews(selector):
    review_containers = selector.xpath('//div[@class="review-container"]')

    reviews = []

    for div in review_containers:
        author_img = div.xpath('.//div[contains(@class, "ui_avatar")]/img/@data-lazyurl').get()
        author_name = div.xpath('.//div[contains(@class, "info_text")]/div/text()').get()

        raiting = div.xpath('.//span[contains(@class, "ui_bubble_rating")]/@class')
        raiting = int(raiting.get()[-2])

        raiting_date = div.xpath('.//span[@class="ratingDate"]/@title').get()

        review_title = div.xpath('.//span[@class="noQuotes"]/text()').get()

        review_text = div.xpath('.//p[@class="partial_entry"]')
        additional_text = review_text.xpath('span/text()').get()
        review_text = review_text.xpath('text()').get()
        if additional_text:
            review_text += additional_text

        reviews.append({
            'author_name': author_name,
            'author_img': author_img,
            'raiting': raiting,
            'review_title': review_title,
            'review_text': review_text
        })

    return reviews



