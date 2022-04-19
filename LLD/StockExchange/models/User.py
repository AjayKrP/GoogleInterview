from abc import ABC
from enum import Enum
from collections import defaultdict

import uuid as uuid


class UserType(Enum):
    DEFAULT, ADMIN = 0, 1


class Address:
    city: str
    zipcode: str
    country: str
    state: str


class User:
    id: uuid.UUID
    name: str
    address: Address
    user_type: UserType.DEFAULT

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.amount = 0
        self.stocks = {}

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def update_amount(self, amount):
        self.amount += amount

    def get_user_name(self):
        return self.name

    def get_id(self):
        return self.id

    def add_stock(self, stock, qty):
        self.stocks[stock.uuid] = self.stocks.get(stock.uuid, 0) + qty
        print(f'You have {self.stocks[stock.uuid]} total stock of the company {stock.name}')
        return True

    def remove_stock(self, stock, qty):
        print(stock.uuid,qty)
        print(self.stocks.get(stock.uuid, 0))
        if self.stocks.get(stock.uuid, 0) - qty >= 0:
            self.stocks[stock.uuid] -= qty
        else:
            return False
        if self.stocks.get(stock.uuid, 0) == 0:
            self.stocks.pop(stock.uuid)
        total = stock.get_price() * qty
        self.update_amount(total)
        return True
