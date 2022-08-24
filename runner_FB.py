from core.sync_client.publisher import Publisher
from scrapers.scraper_AW.config import SERVICE_NAME_FB


def start_script():
    urls = [
        # 'https://www.facebook.com/Ace-Florist-Flower-Delivery-405310066217577/',
        # 'https://www.facebook.com/123PrintingWallaWalla/',
        # 'https://www.facebook.com/pages/category/Education/123-Grow-With-Me-llc-162383013780268/',
        # 'https://www.facebook.com/123HAIRJUPITER/',
        # 'https://m.facebook.com/Bayouwrecker/',
        # 'https://www.facebook.com/LansLapels/',
        # 'https://business.facebook.com/trailcafegrill/',
        # 'https://www.facebook.com/183lanes/',
        # 'https://www.facebook.com/Huntsvilletint/',
        #
        # 'https://facebook.com/Bayouwrecker/',
        # 'https://www.facebook.com/AspenDentalTroyOH/',
        # 'https://www.facebook.com/1-Auto-Salvage-158016870908762/',
        # 'https://www.facebook.com/MaacoLasVegasNV/',
        # 'https://www.facebook.com/96903489015/',
        # 'https://www.facebook.com/1dayresume/',
        # 'https://www.facebook.com/chicagoremodeling/',
        # 'https://www.facebook.com/photoproboca/',
        # 'https://www.facebook.com/Primminailspa-101200398073489/',
        # 'https://www.facebook.com/about/?ref=page_internal',
        # 'https://www.facebook.com/1stafftraining/',
        # 'https://www.facebook.com/1-sign-designs-1425599501001606/',
        # 'https://www.facebook.com/Easy-go-auto-sales-112886773555571/',
        # 'https://www.facebook.com/1-Star-Motors-Inc-761035680594557/',
        # 'https://www.facebook.com/onestoptonerinkjet/',
        # 'https://www.facebook.com/RobertLord88/',
        # 'https://www.facebook.com/DesertCareAnimalHospital/',
        # 'https://www.facebook.com/1-STOP-SIGNS-580051055469726/',
        # 'https://www.facebook.com/1stopmuffler/',
        # 'https://www.facebook.com/181anygarmentcleaners/',
        # 'https://www.facebook.com/10creativetipsntoes/',
        # 'https://www.facebook.com/TonyLocosRestaurant/',
        # 'https://www.facebook.com/1031inc/',
        # 'https://www.facebook.com/10WestSalon/',
        # 'https://www.facebook.com/SacramentoAMP/',
        # 'https://www.facebook.com/100middletn/',
        # 'https://www.facebook.com/OneHundredClub/',
        # 'https://www.facebook.com/alist100kids/',
        # 'https://facebook.com/RAFTMONTANA/events',
        # 'https://www.facebook.com/101autobody/',
        # 'https://www.facebook.com/PYC.LLC.Cleaners/',
        # 'https://www.facebook.com/JimJames101Club/',
        # 'https://www.facebook.com/101coffeeshop/',
        # 'https://www.facebook.com/101DriveIn/',
        # 'https://www.facebook.com/101livestockauction/',
        # 'https://www.facebook.com/101-Physical-Therapy-Inc-977436252312931/',
        # 'https://www.facebook.com/103west/',
        # 'https://www.facebook.com/TenPointAutoService/',
        # 'https://www.facebook.com/1078gallery/',
        # 'https://www.facebook.com/10th-Street-Auto-Body-Specialties-161116257242125/',
        # 'https://www.facebook.com/109barandsteakouse/',
        # 'https://www.facebook.com/southsidebuildingcenter/',
        # 'https://www.facebook.com/prostylezbarber/',
        # 'https://www.facebook.com/10th.st.baking.co/',
        # 'https://www.facebook.com/10thstreettire/',
        # 'https://www.facebook.com/10thAvePizzaCafe/',

        'https://www.facebook.com/PaneraBreadSyossetNY/',
        'https://www.facebook.com/mariosofsyosset/',
        'https://www.facebook.com/Cardinali-Bakery-of-Syosset-321095754583067/',
        'https://en-gb.facebook.com/Mrprestigeli/',
        'https://www.facebook.com/Ace-Florist-Flower-Delivery-405310066217577/'
    ]
    for url in urls:
        task = {
            'request': {
                'callback': 'start',
                'url': url
            }
        }

        publisher(task, SERVICE_NAME_FB)


if __name__ == '__main__':
    publisher = Publisher()
    start_script()
