from abc import ABC, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    SMALL = 0
    MEDIUM = 2
    LARGE = 3


class Vehicle(ABC):
    parkingSpots: []
    licence_plate: str
    spot_needed: 0
    vehicleSize: VehicleSize

    def __init__(self, spot_needed, size):
        self.spot_needed = spot_needed
        self.vehicleSize = size

    def getVehicleSize(self):
        return self.vehicleSize

    def getSpotNeeded(self):
        return self.spot_needed

    def parkInSpots(self, parkingSpot):
        pass

    def clearSpots(self):
        pass

    @abstractmethod
    def canFitInSpot(self, parkingSpot):
        pass


class Bike(Vehicle):
    def __init__(self):
        super(Bike, self).__init__(1, VehicleSize.SMALL)

    def canFitInSpot(self, parkingSpot):
        pass


class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__(2, VehicleSize.MEDIUM)

    def canFitInSpot(self, parkingSpot):
        pass


class Bus(Vehicle):
    def __init__(self):
        super(Bus, self).__init__(5, VehicleSize.LARGE)

    def canFitInSpot(self, parkingSpot):
        pass


class ParkingLot:
    def __init__(self, name):
        self.levels = []
        self.name = name
        self.NUMBER_OF_LEVELS = 5

    def parkVehicle(self, vehicle):
        pass


class Level:
    def __init__(self, lvl):
        self.parking_slots = []
        self.floor = 0
        self.available_spots = 0
        self.SPOT_PER_ROW = 10

    def __int__(self, flr, numberSpots):
        self.floor = flr
        self.available_spots = numberSpots

    def findAvailableSpots(self, vehicle):
        pass

    def parkVehicle(self, vehicle):
        pass

    def parkStartAtSpot(self, vehicle, n):
        pass

    def spotFreed(self):
        self.available_spots += 1


class ParkingSpot:
    vehicle: Vehicle
    vehicleSize: VehicleSize
    row: int
    spotNumber: int
    level: Level

    def __init__(self, lvl, r, n, size):
        self.level = lvl
        self.row = r
        self.vehicleSize = size
        self.spotNumber = n

    def isAvailable(self):
        return self.vehicle is None

    def canFitVehicle(self, vehicle):
        pass

    def removeVehicle(self):
        pass

    def park(self, vehicle):
        pass
