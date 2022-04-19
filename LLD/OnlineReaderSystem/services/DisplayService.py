from OnlineReaderSystem.models.Book import Book
from OnlineReaderSystem.models.User import User


class DisplayService:
    def __init__(self):
        self.__active_book = None
        self.__active_user = None
        self.__pageNumber = 0

    def display_user(self, user: User):
        self.__active_user = user
        self.__refresh_user()

    def __refresh_user(self):
        print(f'current user is: {self.__active_user}')

    def display_book(self, book: Book):
        self.__active_book = book
        self.__refreshTitle()
        self.__refreshDetails()
        self.__refreshPage()

    def __refreshTitle(self):
        print(f'current Book is: {self.__active_book.get_id()}')

    def __refreshDetails(self):
        print(f'current user is: {self.__active_book.get_book_name()}')

    def __refreshPage(self):
        print(f'current page is: {self.__pageNumber}')
