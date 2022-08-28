from core.sync_client.publisher import Publisher
from scrapers.scraper_AW.config import SERVICE_NAME_FB, SERVICE_NAME_FOURSQUARE


def start_script():
    urls = [

        'https://foursquare.com/v/cardinali-bakery/4bb7640c941ad13abd9520e3',
        'https://foursquare.com/v/ace-florist-of-syosset/4e9f2259775b7e725ba4f344',
        'https://foursquare.com/v/marios-pizzeria/4bab8904f964a52053b13ae3',
        'https://foursquare.com/v/ferraris-auto/4c65d9aa9cb82d7f14238fd2',
        'https://foursquare.com/v/panera-bread/50015c6ae4b0b1602b9025a2'
    ]
    for url in urls:
        task = {
            'request': {
                'callback': 'start',
                'url': url
            }
        }

        publisher(task, SERVICE_NAME_FOURSQUARE)


if __name__ == '__main__':
    publisher = Publisher()
    start_script()
