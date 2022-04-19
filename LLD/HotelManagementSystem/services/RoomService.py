from LLD.HotelManagementSystem.models.Room import *
from LLD.HotelManagementSystem.models.Hotel import *

PER_ROOM_COSTS = 500


class RoomService:
    def __init__(self, hotel):
        self.__current_hotel = hotel

    """
    Room Allocation Algorithm
    """
    def book_room(self, user, no_of_guests):
        needed_rooms = self.__get_total_room_needed(no_of_guests)
        amount_to_be_paid = self.__get_room_fare(needed_rooms)
        for floor in range(TOTAL_NUMBER_OF_FLOOR):
            for room in range(MAX_ROOMS_ON_FLOOR):
                if self.__current_hotel.get_rooms()[floor][room].is_vacant and needed_rooms > 0:
                    self.__current_hotel.get_rooms()[floor][room].allocated_user = user
                    self.__current_hotel.get_rooms()[floor][room].is_vacant = False
                    needed_rooms -= 1
                if needed_rooms == 0:
                    break
        return amount_to_be_paid if needed_rooms == 0 else self.vacant_room(user)

    @staticmethod
    def __get_total_room_needed(no_of_guests):
        total = no_of_guests // MAX_CAPACITY_OF_ROOM
        needed_rooms = no_of_guests % MAX_CAPACITY_OF_ROOM
        return total if needed_rooms == 0 else total + 1

    def vacant_room(self, user):
        for floor in range(TOTAL_NUMBER_OF_FLOOR):
            for room in range(MAX_ROOMS_ON_FLOOR):
                if not self.__current_hotel.get_rooms()[floor][room].is_vacant and \
                        user.get_userId == self.__current_hotel.get_rooms()[floor][room].get_userId():
                    self.__current_hotel.get_rooms()[floor][room].allocated_user = None

        return True

    @staticmethod
    def __get_room_fare(number_of_rooms):
        return PER_ROOM_COSTS * number_of_rooms
