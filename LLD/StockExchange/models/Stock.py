import uuid
from abc import ABC


class Stock(ABC):
    uuid: uuid.UUID
    current_price: int
    name: str
    listing_date: str

    def __init__(self, current_price, name):
        self.uuid = uuid.uuid4()
        self.current_price = current_price
        self.name = name

    def set_price(self, price):
        self.current_price = price

    def get_price(self):
        return self.current_price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def update_price(self, change):
        self.current_price += change
