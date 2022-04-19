from LLD.StockExchange.services.PaymentService import PaymentService


class TradingService:
    def __init__(self):
        self.current_stock = None
        self.current_user = None
        self.payment_service = PaymentService()

    def buy_stock(self, qty):
        if self.current_stock and self.current_user:
            total_amount = self.current_stock.get_price() * qty  # TODO add amount in the user profile as well and check if its exceeding total amount
            if self.payment_service.make_payment(total_amount, self.current_user):
                self.current_user.add_stock(self.current_stock, qty)
                print(f'Successfully bought stock {self.current_stock.name}')
                return True
            print('You don\'t have sufficient fund!')
            return False
        else:
            print(f'Something went wrong. Invalid current stock or user')
            return False

    def sell_stock(self, qty):
        if self.current_stock and self.current_user:
            return self.current_user.remove_stock(self.current_stock, qty)
        else:
            print(f'Something went wrong. Invalid current stock or user')
            return False
