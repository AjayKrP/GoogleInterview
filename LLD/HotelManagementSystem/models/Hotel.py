from LLD.HotelManagementSystem.models.Room import Room

MAX_ROOMS_ON_FLOOR = 10
TOTAL_NUMBER_OF_FLOOR = 5


class Hotel:
    def __init__(self, id, name, address):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__rooms = [[Room(f'{i}-{j}') for i in range(MAX_ROOMS_ON_FLOOR)] for j in range(TOTAL_NUMBER_OF_FLOOR)]

    def get_rooms(self):
        return self.__rooms
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_vacant_rooms(self):
        vacant_rooms = []
        for floor in range(TOTAL_NUMBER_OF_FLOOR):
            for room in range(MAX_ROOMS_ON_FLOOR):
                if self.__rooms[floor][room].is_vacant:
                    vacant_rooms.append(f'{floor}-{room}')
        return vacant_rooms
