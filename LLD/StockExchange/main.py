from LLD.StockExchange.models.Stock import Stock
from LLD.StockExchange.models.StockExchange import StockExchange
from LLD.StockExchange.services.TradingService import TradingService
from LLD.StockExchange.services.UserManagementService import UserManager

from LLD.StockExchange.models.User import User

if __name__ == "__main__":
    stock_exchange = StockExchange('NSE')
    stock1, stock2 = Stock(30, 'XYZ'), Stock(50, 'ABC')
    stock_exchange.stocks.append(stock1)
    stock_exchange.stocks.append(stock2)
    user1 = User('ajay')
    um = UserManager()
    um.add_user(user1)
    ts1 = TradingService()
    ts1.current_user = user1
    ts1.current_stock = stock1

    ts1.buy_stock(4)
    ts1.buy_stock(8)
    ts1.sell_stock(2)

    user1.set_amount(500)
    ts1.buy_stock(4)
    ts1.current_stock = stock2
    ts1.buy_stock(8)
    ts1.current_stock = stock1
    ts1.sell_stock(2)
    print(user1.get_amount())
    print(user1.stocks)
