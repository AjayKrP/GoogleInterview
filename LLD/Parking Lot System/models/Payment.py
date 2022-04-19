from enum import Enum


class PaymentStatus(Enum):
    SUCCESS = 1
    FAILED = 2
    PENDING = 3


class Payment:
    def __init__(self, id, amount, status=PaymentStatus.PENDING):
        self.id = id
        self.amount = amount
        self.status = status
