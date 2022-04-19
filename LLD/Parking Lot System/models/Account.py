from abc import ABC
from enum import Enum
from .ParkingFloor import ParkingFloor
from .Spot import Spot
from .Ticket import Ticket
from .User import User


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    BLOCKED = 3
    UNVERIFIED = 4


class Account(ABC):
    username: str
    password: str
    status: AccountStatus
    user: User

    def reset_password(self):
        pass


class Admin(Account):
    def add_parking_floor(self, parkingFloor: ParkingFloor):
        pass

    def add_parking_spot(self, spot: Spot):
        pass


class ParkingAttendant(Account):
    def process_ticket(self, ticket: Ticket):
        pass
