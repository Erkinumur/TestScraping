from core.sync_client.publisher import Publisher
from scrapers.scraper_AW.config import SERVICE_NAME_FB, SERVICE_NAME_FOURSQUARE, SERVICE_NAME_YELP


def start_script():
    urls = [

        'https://www.yelp.com/biz/cardinali-bakery-syosset',
        'https://www.yelp.com/biz/ace-florist-and-flower-delivery-syosset',
        'https://www.yelp.com/biz/marios-pizzeria-syosset',
        'https://www.yelp.com/biz/ferrari-auto-repair-syosset',
        'https://www.yelp.com/biz/panera-bread-syosset',
        'https://www.yelp.com/biz/marks-barber-shop-syosset',
        'https://www.yelp.com/biz/kaplan-lawyers-pc-syosset-4',
        'https://www.yelp.com/biz/mr-prestige-syosset',

        'https://www.yelp.com/biz/brian-j-levy-and-associates-the-bronx'
    ]
    for url in urls:
        task = {
            'request': {
                'callback': 'start',
                'url': url
            }
        }

        publisher(task, SERVICE_NAME_YELP)


if __name__ == '__main__':
    publisher = Publisher()
    start_script()
