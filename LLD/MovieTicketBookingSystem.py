"""
Actors
1. User/Customer/Admin/Front Desk Officer
2. System

Person
    - Admin - add movie, add cinema hall
    - frontdesk officer - create booking/search movie/cancel booking
    - User - search movie
    - Customer - create booking/search movie/cancel booking
Movie
Theater
CinemaHall
Seat
City
Booking
Payment
Ticket
"""
from abc import ABC, abstractmethod
from enum import Enum


class Person(ABC):
    def __init__(self, id, name, phone, email):
        pass


class Admin(Person):
    def add_movie(self, movie):
        pass

    def remove_movie(self):
        pass

    def add_cinema_hall(self, cinema_hall):
        pass


class Customer(Person):
    def __init__(self, id, name, phone, email):
        super().__init__(id, name, phone, email)
        self.search = Search()
        self.booking = None

    def makeBooking(self, city, theater, movie):
        pass

    def showBooking(self):
        pass


class FrontDeskOfficer(Person):
    def __init__(self, id, name, phone, email):
        super().__init__(id, name, phone, email)
        self.search = Search()
        self.booking = None

    def createBooking(self):
        pass


class City:
    def __init__(self, id, name, pincode, state, country):
        self.__id = id
        self.__name = name
        self.__pincode = pincode
        self.__state = state
        self.__country = country
        self.theaters = []

    def getTheaters(self):
        pass


class Movie:
    def __init__(self, name, genres, actors, release_date):
        self.__name = name
        self.__genres = genres
        self.__actors = actors
        self.__release_date = release_date
        self.__shows = []

    def getShows(self):
        pass


class Show:
  def __init__(self, id, played_at, movie, start_time, end_time):
    self.__show_id = id
    self.__created_on = None
    self.__start_time = start_time
    self.__end_time = end_time
    self.__played_at = played_at
    self.__movie = movie


class Theater:
    def __init__(self):
        self.movies = []
        self.cinema_halls = []


class CinemaHall:
    def __init__(self):
        self.movie = []
        self.seats = []


class SeatType(Enum):
    DELUX = 0
    SILVER = 1
    GOLD = 2


class Seat:
    def __init__(self, type, price):
        self.type = type
        self.price = price


class Catalog:
    def __init__(self):
        self.movies_mapping_by_title = {}
        self.movies_mapping_by_genres = {}
        self.movies_mapping_by_release_date = {}
        self.movies_mapping_by_actors = {}


class SearchType(Enum):
    NAME = 0
    GENRES = 1
    RELEASE_DATE = 2
    ACTORS = 3


class Search(ABC):
    def __init__(self):
        self.catalog = Catalog()

    @abstractmethod
    def search(self, query, type):
        pass


class SearchByName(Search):
    def search(self, query, type=SearchType.Name):
        pass


class SearchByActors(Search):
    def search(self, query, type=SearchType.ACTORS):
        if query in self.catalog.movies_mapping_by_actors:
            return self.catalog.movies_mapping_by_actors[query]
        return None


class SearchByReleaseDate(Search):
    def search(self, query, type=SearchType.RELEASE_DATE):
        pass


class Ticket:
    def __init__(self, id, seats):
        self.__id = id
        self.__seats = seats

    def getTicketPrice(self):
        total = 0
        for seat in self.__seats:
            total += seat.price
        return total


class Booking:
    def __init__(self, id, ticket):
        self.__id = id
        self.__ticket = ticket

    def getTotalAmountToPay(self):
        # Add Tax + ticket Price
        return self.__ticket.getTicketPrice()


class PaymentStatus(Enum):
    PENDING = 0
    SUCCESS = 1
    FAILURE = 2


class Payment:
    def __init__(self, id, booking, status=PaymentStatus.PENDING):
        self.__id = id
        self.__booking = booking
        self.__status = status

    def cancel_payment(self):
        pass


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        pass


class SMSNotification(Notification):
    def send(self, message):
        pass
