import requests
from fake_useragent import UserAgent
from parsel import Selector

ua = UserAgent()
headers = {'User-agent': ua.chrome}
response = requests.get(url, headers=headers)
selector = Selector(response.text)
