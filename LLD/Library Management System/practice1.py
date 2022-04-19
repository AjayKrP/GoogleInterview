from enum import Enum
from collections import defaultdict
from datetime import timedelta, date

DUE_DATE_OF_BOOK = 7
FINE_PER_DAY = 10


class LendService:
    def __init__(self, user, book):
        self.__user = user
        self.__book = book
        self.lend_book_db = list(defaultdict)

    def get_total_fine(self):
        total_fine = 0
        for book in self.lend_book_db[self.__user]:
            total_date = book.due_date - date.today()
            if total_date < 0:
                total_fine += total_date * FINE_PER_DAY
        return total_fine

    def lend_book(self):
        if self.get_total_fine() > 0:
            self.__book.due_date = date.today() + timedelta(days=DUE_DATE_OF_BOOK)
            self.__user.current_holding_books.append(self.__book)
            self.lend_book_db[self.__user.id].append(self.__book.id)

    def return_book(self):
        if self.__book not in self.lend_book_db[self.__user]:
            raise Exception('Book Not Found on your name.')

        total_fine = self.get_total_fine()
        if total_fine > 0:
            print(f'please pay total fine of {total_fine}.')
        self.lend_book_db[self.__user].remove(self.__book)
        self.__user.current_holding_books.remove(self.__book)
        return True


class UserService:
    def __init__(self):
        current_holding_books = []

    def add_book_to_current_holding(self, book):
        pass


class NotificationService:
    def send_notification(self, message):
        pass


class User:
    def __init__(self, id, name, imageUrl, bio):
        self.id = id
        self.name = name
        self.imageUrl = imageUrl
        self.bio = bio
        self.role = None

    def get_user_by_id(self, id):
        return self


class Book:
    def __init__(self):
        self.book = {}


class BookItem:
    def __init__(self, id, title, author, pages):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
