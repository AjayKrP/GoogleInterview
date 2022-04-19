from enum import Enum


class ParkingTicketStatus(Enum):
    ACTIVE = 1
    EXPIRED = 2
    NONE = 3


class ParkingRate:
    def __init__(self, id, rate, vehicleType, status=ParkingTicketStatus.NONE):
        self.id = id
        self.rate = rate
        self.vehicleType = vehicleType
        self.status = status
