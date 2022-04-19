from collections import defaultdict

from LLD.HotelManagementSystem.models.Transaction import Transaction


class PaymentService:
    def __init__(self):
        self.__transactions = defaultdict(list)

    def make_transaction(self, user, amount):
        self.__transactions[user.get_userId()].append(Transaction(amount))
        return True

    def get_transactions(self, user):
        return self.__transactions[user.get_userId()]
