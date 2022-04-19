from .Vehicle import Vehicle
from enum import Enum


class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class Spot:
    number: str
    free: bool
    vehicle: Vehicle
    type: ParkingSpotType

    def __init__(self, type):
        self.type = type

    def assign_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.free = False

    def remove_vehicle(self):
        self.vehicle = None
        self.free = True


class LargeSpot(Spot):
    def __init__(self):
        super(LargeSpot, self).__init__(ParkingSpotType.LARGE)


class MoterbikeSpot(Spot):
    def __init__(self):
        super(MoterbikeSpot, self).__init__(ParkingSpotType.MOTORBIKE)
