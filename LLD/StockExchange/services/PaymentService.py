from LLD.StockExchange.models.Payment import Payment
from collections import defaultdict


class PaymentService:
    def __init__(self):
        self.txns = defaultdict(list)

    def make_payment(self, amount, user):
        if user.get_amount() - amount >= 0:
            user.update_amount(-amount)
            self.txns[user.id].append(Payment(amount, user.id))
            return True
        return False

    def get_transactions_history(self, user):
        return self.txns[user.id]
