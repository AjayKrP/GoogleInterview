from time import time


class Transaction:
    def __init__(self, amount):
        self.__amount = amount
        self.createdAt = time()

    def get_amount(self):
        return self.__amount
