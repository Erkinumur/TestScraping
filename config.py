import os

from settings import RMQ_EXCHANGE

PREFETCH_COUNT = 10
SERVICE_NAME = RMQ_EXCHANGE + '.scrapers.' + RMQ_EXCHANGE
SERVICE_NAME_FB = SERVICE_NAME + '_FB'
SERVICE_NAME_LINKS = SERVICE_NAME + '_Links'
SERVICE_NAME_YELP = SERVICE_NAME + '_Yelp'
SERVICE_NAME_TA = SERVICE_NAME + '_TA'
SERVICE_NAME_GOOGLE = SERVICE_NAME + '_Google'
SERVICE_NAME_FOURSQUARE = SERVICE_NAME + '_FS'
SERVICE_NAME_SAVER_REVIEWS = 'AW.scrapers.ReviewSaver'
SERVICE_NAME_SAVER_PHOTOS = 'AW.scrapers.PhotoSaver'

DEFAULT_HEADERS_FB = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

DEFAULT_HEADERS_GOOGLE = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189',
    'Accept-Language': 'en-US,en;q=0.9,uk;q=0.8,ru;q=0.7',
    'referer': 'https://www.google.com/',
    'cookie': 'NID=204=remhrSmEnTBQf9IcapTTZgujWIEtuxgXxoIhC52RlaTmC6wJJSkcqTBB3pWaVaHOk3uPqjgEf-zI2'
              'Z36vKO6BS9DeBjx_xR-C_LDnI0WLyHoX1PesOM38Bwx4m88JjSj5tGOS5aQ0J6JiNIdrtYt8Wytl78QvyTFIz6'
              'Y-7Y-_O90OO6WgKML7oJ3qEAwedvFbdbIK8ylVvAzq7Ukk5pR6wp4tYk3v4moZV6qCGMWFjez7P-HTEUhXhqcg'
              'li9CZTNIjLMCHjg3Zu7hDlj5DrAtJ8VUi5K25WraQI75GEKvchN0noA2Nn1AzzmlrFcywIV'
}

DEFAULT_PARAMS = None

PROXY_URL = 'http://lum-auth-token:8BjwW5d4etXa5SbuNzDnWxTFvbAguDzc@5.189.151.227:24001'
# PROXY_URL_GOOGLE = "http://scraperapi:6441f5c7026253e39e10825e1640b59d@proxy-server.scraperapi" \
#                    ".com:8001"
PROXY_URL_GOOGLE = "http://bogdannesterenko8843:1ff381@node-us-27.astroproxy.com:11195"

# PROXY_URL_FB = 'http://scraperapi:d63aa1fb0b952c8a4d8438d64782af3f@proxy-server.scraperapi.com:8001'
PROXY_URL_FB = PROXY_URL

DEFAULT_PROXIES = {
    'http': PROXY_URL_GOOGLE,
    'https': PROXY_URL_GOOGLE
}

DEFAULT_PROXIES_GOOGLE = {
    'http': PROXY_URL_GOOGLE,
    'https': PROXY_URL_GOOGLE
}

DEFAULT_PROXIES_FB = {
    'http': PROXY_URL_FB,
    'https': PROXY_URL_FB
}

DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 300

DB_URL = os.getenv('DB_URL')

PROXY_OXYLAB_USER = 'bogdannesterenko'
PROXY_OXYLAB_PASS = '7tLWtF3bXI2x'