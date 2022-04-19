from abc import ABC, abstractmethod
from enum import Enum
from collections import defaultdict


class Config:
    MAX_ISSUE_LIMIT = 3
    MAX_ISSUE_DAY = 7

    def get_book_hash_code(self, book):
        if book == '':
            raise ValueError('Book Name is empty!')
        return book[0] % 26


class BookFormat(Enum):
    HARDCOVER = 0
    EBOOK = 1


class BookStatus(Enum):
    AVAILABLE = 0
    RESERVED = 1


class ReservationStatus(Enum):
    WAITING = 0
    PENDING = 1
    CANCELED = 2


class AccountStatus(Enum):
    ACTIVE = 0
    INACTIVE = 1
    BLOCKED = 2


class Account(ABC):
    def __init__(self, u_id, email, password):
        self.u_id = u_id
        self.email = email
        self.password = password

    def reset_password(self):
        pass


class Librarian(Account):
    def __init__(self):
        super(Account, self).__init__()
        self.config = Config()

    def add_book_item(self, book):
        rack = Rack()
        book_hash_index = self.config.get_book_hash_code(book)
        rack.racks[book_hash_index].append(book)
        
    def remove_books(self, book):
        rack = Rack()
        book_hash_index = self.config.get_book_hash_code(book)

    def block_user(self, user):
        pass

    def block_issue_book(self, bookItems):
        pass


class Book(ABC):
    def __init__(self, isbn, name, authors, no_of_pages):
        self.isbn = isbn
        self.name = name
        self.authors = authors
        self.no_of_pages = no_of_pages


class BookItem(Book):
    def __init__(self, isbn, name, authors, no_of_pages, barcode):
        super(Book, self).__init__(isbn, name, authors, no_of_pages)
        self.barcode = barcode
        self.status = BookStatus.AVAILABLE

    def get_barcode(self):
        return self.barcode

    def book_status(self):
        return self.status


class Rack:
    def __init__(self):
        self.racks = defaultdict(list)


class Library:
    def __init__(self):
        pass
