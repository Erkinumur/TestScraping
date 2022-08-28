from core.sync_client.publisher import Publisher
from scrapers.scraper_AW.config import SERVICE_NAME_FB, SERVICE_NAME_FOURSQUARE, SERVICE_NAME_YELP, \
    SERVICE_NAME_GOOGLE


def start_script():
    urls = [

        'https://www.google.com/search?q=Cardinali+Bakery+III+Syosset+NY+14+Cold+Spring+Rd+11791',
        'https://www.google.com/search?q=Ace+Florist+Syosset+NY+45+Cold+Spring+Rd+11791',
        'https://www.google.com/search?q=Mario%27s+Pizza+of+Syosset+Syosset+NY+326+Jericho+Tpke+11791',
        'https://www.google.com/search?q=Ferrari+Auto+Repr+Inc+Syosset+NY+160+Jackson+Ave+11791',
        'https://www.google.com/search?q=Panera+Bread+Syosset+NY+407+Jericho+Tpke+11791',
        'https://www.google.com/search?q=Marks+Barber+Shop+Syosset+NY+8A+Jackson+Ave+11791',
        'https://www.google.com/search?q=Kaplan+Lawyers+PC+Syosset+NY+6901+Jericho+Tpke+11791',
        'https://www.google.com/search?q=Galli+%26+Co+Cpa%27s+Syosset+NY+375+Jericho+Tpke+11791',
        'https://www.google.com/search?q=Brian+J+Levy+%26+Associates+PLLC+Syosset+NY+1+Stuart+Dr'
        '+11791',
        'https://www.google.com/search?q=Mr+Prestige+Corp+Syosset+NY+335+Jackson+Ave+11791'
    ]
    for url in urls:
        task = {
            'request': {
                'callback': 'start',
                'url': url
            }
        }

        publisher(task, SERVICE_NAME_GOOGLE)


if __name__ == '__main__':
    publisher = Publisher()
    start_script()
