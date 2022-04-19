from abc import ABC, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

class VehicleType(Enum):
  CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5
# class Vehicle(ABC):
#     def __init__(self, spotNeeded, size):
#         self.numberPlate = None
#         self.spotNeeded = spotNeeded
#         self.size = size
#
#     def get_spot_needed(self):
#         return self.spotNeeded
#
#     def get_size(self):
#         return self.size
#
#     @abstractmethod
#     def can_fit_into_spot(self, spot):
#         pass
#
#
# class Bus(Vehicle):
#     def can_fit_into_spot(self, spot):
#         return spot.size >= self.get_spot_needed()
#
#     def __init__(self):
#         super(Bus, self).__init__(5, VehicleSize.LARGE)
#
#
# class Car(Vehicle):
#     def can_fit_into_spot(self, spot):
#         return spot.size >= self.get_spot_needed()
#
#     def __init__(self):
#         super(Car, self).__init__(1, VehicleSize.MEDIUM)
#
#
# class Motercycle(Vehicle):
#     def can_fit_into_spot(self, spot):
#         return spot.size >= self.get_spot_needed()
#
#     def __init__(self):
#         super(Motercycle, self).__init__(1, VehicleSize.SMALL)


from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, license_number, vehicle_type, ticket=None):
    self.__license_number = license_number
    self.__type = vehicle_type
    self.__ticket = ticket

  def assign_ticket(self, ticket):
    self.__ticket = ticket


class Car(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.CAR, ticket)


class Van(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.VAN, ticket)


class Truck(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.TRUCK, ticket)


