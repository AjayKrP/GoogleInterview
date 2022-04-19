from enum import Enum


class DisplayActions(Enum):
    WITHDRAW = 0
    DEPOSIT = 2
    CHECK_BALANCE = 3


class Display:
    def __init__(self):
        self.actions = DisplayActions
   