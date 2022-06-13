import json
import math
from pprint import pprint

import requests
from fake_useragent import UserAgent
from parsel import Selector

from TestScraping.models import ReviewData

base_url = 'https://www.yelp.com'


def parse_reviews(selector):

    script = selector.xpath('//script[@type="application/ld+json"]')[2]
    data_string = script.get().strip('<script type="application/ld+json">').strip('</script>')
    data = json.loads(data_string)

    return data.get('review')

def get_review_api(company_endpoint):
    url = f'https://www.yelp.com/biz/{company_endpoint}/review_feed'
    params = {
        'rl': 'en',
        'sort_by': 'relevance_desc',
        'start': 0
    }

    response = requests.get(url, params=params)
    data = response.json()
    reviews = data.get('reviews')

    results_per_page = data.get('pagination').get('resultsPerPage')
    total_results = data.get('pagination').get('totalResults')

    if total_results > results_per_page:
        pages = math.ceil(total_results / results_per_page)
        start = results_per_page
        for i in range(pages):
            params['start'] = start
            response = requests.get(url, params=params)
            reviews.extend(response.json().get('reviews'))
            start += results_per_page

    result = []
    for i in reviews:
        result.append(get_review_model_from_json(i))

    return result

def get_review_model_from_json(data):
    owner_data = data.get('user')

    review = ReviewData(
        author_name=owner_data.get('markupDisplayName'),
        author_url=base_url + owner_data.get('link'),
        author_photo_url=owner_data.get('src'),
        created_at=data.get('localizedDate'),
        raiting=data.get('rating'),
        text=data.get('comment').get('text')
    )

    return review



if __name__ == '__main__':
    # url = 'https://www.yelp.com/biz/ace-florist-syosset-4'
    # ua = UserAgent()
    # headers = {'User-agent': ua.chrome}
    # response = requests.get(url, headers=headers)
    # selector = Selector(response.text)
    #
    # reviews = parse_reviews(selector)
    #

    reviews = get_review_api('ace-florist-syosset-4')

    with open('yelp.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps([i.__dict__ for i in reviews], ensure_ascii=False))

    print(len(reviews))
