from datetime import datetime
from random import random


class Txn:
    def __init__(self, amount):
        self.id = random()
        self.amount = amount
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_txn_amount(self, id):
        return self.amount

    def update_txn_amount(self, amount):
        self.amount = amount
        self.update_txn_time()
        return True

    def update_txn_time(self):
        self.updated_at = datetime.now()
