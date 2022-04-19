from enum import Enum


class Hotel:
    def __int__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []


class Location:
    def __init__(self, street, city, pincode, country):
        pass


class RoomType(Enum):
    DELUX = 1
    AC = 2


class RoomStatus(Enum):
    BOOKED = 0
    NOT_BOOKED = 1


class RoomStyle(Enum):
    A = 1
    B = 2


class Room:
    def __init__(self, room_number, room_price, type=RoomType.DELUX, style=RoomStyle.A, status=RoomStatus.NOT_BOOKED):
        self.room_number = room_number
        self.room_price = room_price
        self.room_keys = []
        self.house_keeping_logs = []


class Booking:
    def __init__(self, room_number, checkin_date, num_of_guests, rooms):
        pass


class Payment:
    def __init__(self, amount, booking_id):
        pass


class RoomKey:
    def __init__(self, keyId, barCode, issueAt, isActive, isMaster):
        pass

    def assignRoom(self, room):
        pass

class HouseKeepingLogs:
    def __init__(self, description, startDate, duration, houseKeeper):
        pass

    def addRoom(self, room):
        pass

from abc import ABC

class Person(ABC):
    def __init__(self, name, account_detail, phone):
        pass

class Account:
    def __init__(self, username, password, is_active):
        pass

class Housekeeper(Person):
    def getRoomServiced(self, date):
        pass


class Guest(Person):
    def __init__(self):
        self.search = None
        self.booking = None

    def getBookedRooms(self):
        pass
class Receptionist(Person):
    def __init__(self):
        self.search = None
        self.booking = None

    def checkInGuest(self, guest, room_booking):
        pass

    def checkoutGuest(self, guest, room_booking):
        pass

class Admin(Person):
    def addRoom(self, room):
        pass

    def deleteRoom(self, room):
        pass

    def editRoom(self, room):
        pass


class Search:
    def searchRooms(self, style, type, date):
        pass

class Booking:
    def createBooking(self, guestInfo):
        pass

    def cancelBooking(self, bookingId):
        pass

class RoomBooking:


