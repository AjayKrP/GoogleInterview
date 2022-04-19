from .Vehicle import Vehicle

class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}

    def add_spot(self, spot):
        pass

    def remove_spot(self, spot):
        pass

    def assign_vehicle(self, spot, vehicle: Vehicle):
        pass

