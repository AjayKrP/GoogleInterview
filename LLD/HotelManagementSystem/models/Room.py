MAX_CAPACITY_OF_ROOM = 2


class Room:
    def __init__(self, room_no, capacity=MAX_CAPACITY_OF_ROOM):
        self.__room_no = room_no
        self.__capacity = capacity
        self.is_vacant = True
        self.allocated_user = None

    def __str__(self):
        return f'Current room is: {self.__room_no}'

