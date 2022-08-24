from core.sync_client.publisher import Publisher
from scrapers.scraper_AW.config import SERVICE_NAME_TA


def start_script():
    urls = [
        # 'https://www.tripadvisor.com/Restaurant_Review-g295424-d10336417-'
        # 'Reviews-Couqley_French_Bistro_Dubai-Dubai_Emirate_of_Dubai.html'

        # 'https://www.tripadvisor.com/Restaurant_Review-g60713-d4253461-'
        # 'Reviews-Lee_s_Deli-San_Francisco_California.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g34515-d1059610-'
        # 'Reviews-Fresco_Cucina_Italiana-Orlando_Florida.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g29171-d426678-'
        # 'Reviews-168_Chinese_Restaurant-Apopka_Florida.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g33804-d15170701-'
        # 'Reviews-No_1_China_Palace-Hartford_Connecticut.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g29161-d4401584-'
        # 'Reviews-No_1_Chinese_Take_Out-Altamonte_Springs_Florida.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g46361-d4613628-'
        # 'Reviews-No_1_China_Chinese_Restaurant-Clementon_New_Jersey.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g41317-d5587032-'
        # 'Reviews-No_1_Chinese_Kitchen-Pikesville_Maryland.html',
        # 'https://www.tripadvisor.com/Restaurant_Review-g29810-d10475272-'
        # 'Reviews-Crystal_Asian_Cuisine-Amherst_New_York.html',
        # 'https://www.tripadvisor.com/Hotel_Review-g32668-d10687656-'
        # 'Reviews-El_Dorado_Inn-Lynwood_California.html',

        'https://www.tripadvisor.com/Restaurant_Review-g48712-d4929218-'
        'Reviews-Panera_Bread-Syosset_Long_Island_New_York.html',
        'https://www.tripadvisor.com/Restaurant_Review-g48712-d830339-'
        'Reviews-Mario_s_Pizzeria-Syosset_Long_Island_New_York.html',
        'https://www.tripadvisor.com/Restaurant_Review-g48712-d4980571-'
        'Reviews-Cardinali_Bakery-Syosset_Long_Island_New_York.html'
    ]
    for url in urls:
        task = {
            'request': {
                'callback': 'start',
                'url': url
            }
        }

        publisher(task, SERVICE_NAME_TA)


if __name__ == '__main__':
    publisher = Publisher()
    start_script()
