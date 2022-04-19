from LLD.ATM.models.Display import Display
from LLD.ATM.models.Keyboard import Keyboard
from LLD.ATM.models.MoneyTaker import MoneyTaker
from LLD.ATM.models.ReceiptTaker import ReceiptTaker


class ATM:
    _instance = None

    class OnlyOne:
        def __init__(self):
            pass

    def __init__(self, name, bankcode):
        if ATM._instance is None:
            self.name = name
            self.bank_code = bankcode
            self.display = Display()
            self.receipt_window = ReceiptTaker()
            self.keyboard = Keyboard()
            self.money_taker_window = MoneyTaker()
            ATM._instance = ATM.OnlyOne()

    def authenticate_user(self):
        pass
