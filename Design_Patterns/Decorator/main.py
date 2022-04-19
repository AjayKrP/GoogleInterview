from abc import ABC, ABCMeta


class Component(ABC):
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "Concrete Component"


class Decorator(Component):
    def __init__(self, wrapee):
        self.__wrapee = wrapee

    def operation(self):
        self.__wrapee.opeation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        pass


class ConcreteDecoratorB(Decorator):
    def operation(self):
        pass


if __name__ == "__main__":
    cc = ConcreteComponent()
    cca = ConcreteDecoratorA(cc)
    ccb = ConcreteDecoratorB(cca)

"""
AMCV_8F99160E571FC0427F000101%40AdobeOrg=1585540135%7CMCIDTS%7C18811%7CMCMID%7C47782007312565129901190473715952404877%7CMCAAMLH-1625818240%7C12%7CMCAAMB-1625818240%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1625220640s%7CNONE%7CMCSYNCSOP%7C411-18818%7CvVersion%7C4.4.0; _hiUPgpMP11=eyJzaXBsdWlkIjoiWVRNNVlqazNZVGd0WWprNU15MDBNVEF6TFRobVpETXRZemRpTURVMFltTTFaVEZrIiwic2lwbHZyc24iOiJNZz09Iiwic2lwbHN0cmNkIjoiTURjMU5XVmlZVFl0TkdRNVlpMDBNRFJqTFRobVkyTXRZekJrT0RVNU5tUXlORGt6In0=; private_content_version=6a43cb06a0529394261d2f196ad6d674; userPincode=560010; userPincodeGroupName=Bangalore; userPincodeServiceAvailable=1; STVID=8b983b67-d033-ea6a-fc3e-537a7dea04df; form_key=RR8iQKO7DFlREPVo; siplssid={\"content\":\"4b3c0fff-38dd-4e82-a8d8-5e8681881f0b\"}; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; mage-cache-sessid=true; mage-messages=; amplitude_idshoptimize.in=eyJkZXZpY2VJZCI6ImM1YmM0NzY1LTcwYzktNGEyMy1iNjU1LTgzOGExZjVmYmQzY1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYyNjU5ODA0NDA5OSwibGFzdEV2ZW50VGltZSI6MTYyNjU5ODEyMDM3NSwiZXZlbnRJZCI6NzAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjo3MH0=; _pk_id.0755eba6-4d9b-404c-8fcc-c0d8596d2493.db35=e9f060863d2496be.1626278563.3.1626598121.1626598044.; _pk_ses.0755eba6-4d9b-404c-8fcc-c0d8596d2493.db35=*; _ga=GA1.2.475744644.1624968408; _gid=GA1.2.963698189.1626598043; _gat=1; _clck=izxkwo; STUID=1b2103bf-3ea1-a5f9-98ed-230ef4cc8edf; _gcl_au=1.1.194655704.1624968407; _gat_gtag_UA_185027859_1=1; _clsk=bfxg33|1626598124568|2|1|eus/collect; section_data_ids=%7B%22customer%22%3A1626598122%2C%22compare-products%22%3A1626598122%2C%22last-ordered-items%22%3A1626598122%2C%22cart%22%3A1626598122%2C%22directory-data%22%3A1626598122%2C%22review%22%3A1626598122%2C%22wishlist%22%3A1626598122%2C%22rewards%22%3A1626598122%2C%22paypal-billing-agreement%22%3A1626598122%7D; TawkConnectionTime=1626598141821
"""