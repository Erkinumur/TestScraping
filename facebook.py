import json
from pprint import pprint

import requests
from parsel import Selector

from google_reviews import proxies
from models import ReviewData

# url = "https://www.facebook.com/Ace-Florist-405310066217577/reviews/"
url = 'https://www.facebook.com/CouqleyUAE/reviews/'
graphql_url = 'https://www.facebook.com/api/graphql/'

graphql_params = {'doc_id': 7751838121557253}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

variables = {"count": 5, "feedLocation": "PAGE_TIMELINE", "feedbackSource": 0,
             "privacySelectorRenderLocation": "COMET_STREAM", "renderLocation": "permalink",
             "scale": 1, "sort_order": "MOST_HELPFUL"}
doc_id = 7751838121557253

response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
selector = Selector(response.text)


def parse_html_data(selector):
    script = selector.xpath('//script[contains(text(), "local_rec_pattern_cursor")]/text()').get()
    data = script.split('CometPageReviews')[-1]
    data = data[data.find('{'):]
    data = data.split(']],["CometUFI')[0]
    data = json.loads(data)

    reviews_data = data['__bbox']['result']['data']['page']['reviews_recommendations_feed']['edges']
    reviews_data = [i['node'] for i in reviews_data]
    page_info = data['__bbox']['result']['data']['page']['reviews_recommendations_feed'][
        'page_info']

    reviews = []

    for review in reviews_data:
        text = review['comet_sections']['content']['story']['comet_sections']['message']['story'][
            'message']['text']

        author_data = review['comet_sections']['context_layout']['story']['comet_sections'][
            'actor_photo']['story']['actors'][0]

        author_photo_url = author_data['profile_picture']['uri']
        author_url = author_data['profile_url']
        author_name = author_data['name']

        created_at = review['comet_sections']['context_layout']['story']['comet_sections'][
            'metadata'][0]['story']['creation_time']

        reviews.append(ReviewData(
            author_name=author_name,
            author_photo_url=author_photo_url,
            text=text,
            author_url=author_url,
            created_at=created_at
        ))

    reviews.extend(get_reviews_from_graphql(data))

    return reviews


def get_reviews_from_graphql(data: dict):
    data = data.copy()
    page_info = data['__bbox']['result']['data']['page']['reviews_recommendations_feed'][
        'page_info']
    id = data['__bbox']['result']['data']['page']['id']

    count = 1
    reviews = []

    while page_info['has_next_page']:
        print(page_info['has_next_page'])
        cursor = page_info['end_cursor']

        variables_ = variables.copy()
        variables_.update({'cursor': cursor, 'id': id})

        payload = {"doc_id": doc_id, "variables": json.dumps(variables_)}

        attempts = 1

        while True:
            try:
                res = requests.post(
                    graphql_url, headers=headers, proxies=proxies, data=payload, timeout=10
                )
                data = res.json()
                print(count)
                print(data.keys())
                reviews_data = data['data']['node']['reviews_recommendations_feed']['edges']
                reviews_data = [i['node'] for i in reviews_data]
            except Exception as e:
                print(f'Exception: {e}')
                if attempts > 5:
                    break
                attempts += 1
                continue
            else:
                if attempts > 5:
                    break
                if None in reviews_data:
                    print('No reviews')
                    pprint(payload)
                    attempts += 1
                    continue
                else:
                    break
        if attempts > 5:
            break

        page_info = data['data']['node']['reviews_recommendations_feed']['page_info']

        for review in reviews_data:
            text = review['comet_sections']['content']['story']['comet_sections']['message']
            if text:
                text = text['story']['message']['text']

            author_data = review['comet_sections']['context_layout']['story']['comet_sections'][
                'actor_photo']['story']['actors'][0]

            author_photo_url = author_data['profile_picture']['uri']
            author_url = author_data['profile_url']
            author_name = author_data['name']

            created_at = review['comet_sections']['context_layout']['story']['comet_sections'][
                'metadata'][0]['story']['creation_time']

            reviews.append(ReviewData(
                author_name=author_name,
                author_photo_url=author_photo_url,
                text=text,
                author_url=author_url,
                created_at=created_at
            ))

        count += 1

    return reviews


if __name__ == '__main__':
    reviews = parse_html_data(selector)

    with open('facebook.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps([i.__dict__ for i in reviews], ensure_ascii=False))

    print(len(reviews))
