import random


class Payment:
    def __init__(self, amount, user_id):
        self.txn_id = str(random.random())
        self.amount = amount
        self.user_id = user_id

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def get_user(self):
        return self.user_id
