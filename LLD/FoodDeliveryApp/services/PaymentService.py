from LLD.FoodDeliveryApp.models.Txn import Txn


class PaymentService:
    def __init__(self, user):
        self.user = user
        self.transactions = []

    def make_transaction(self, amount):
        self.transactions.append({'user': self.user, 'txn': Txn(amount)})

    def get_transactions(self):
        pass
