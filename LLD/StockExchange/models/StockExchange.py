from collections import defaultdict


class StockExchange:
    _instance = None

    class OnlyOne:
        def __init__(self, name):
            pass

    def __init__(self, name):
        if not StockExchange._instance:
            self.name = name
            self.stocks = []  # dictionary of stocks
            StockExchange._instance = self.OnlyOne(name)

    def get_listed_companies(self):
        return self.stocks

    def add_stock(self, stock):
        if stock not in self.stocks:
            self.stocks.append(stock)
            return True
        return False
    
    def remove_stock(self, stock):
        if stock in self.stocks:
            self.stocks.pop(stock.uuid)
            return True
        return False
