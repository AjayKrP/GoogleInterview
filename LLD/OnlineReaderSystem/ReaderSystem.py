from services.LibraryService import *
from services.UserService import *
from services.DisplayService import *


class ReaderSystem:
    def __init__(self):
        self.__library_service = LibraryService()
        self.__user_service = UserService()
        self.__display_service = DisplayService()
        self.__active_book = None
        self.__active_user = None

    def getLibrary(self):
        return self.__library_service

    def getDisplay(self):
        return self.__display_service

    def getUsers(self):
        return self.__user_service

    def setActiveBooks(self, book: Book):
        self.__active_book = book
        self.__display_service.display_book(book)

    def setActiveUser(self, user: User):
        self.__active_user = user
        self.__display_service.display_user(user)

    def getActiveUser(self):
        return self.__active_user

    def getActiveBook(self):
        return self.__active_book


if __name__ == "__main__":
    ls = ReaderSystem()

    user1 = User('ajayk', 'Ajay$123$')
    user2 = User('deepak', 'Ajay$123$')
    ls.getUsers().add_user(user1)
    ls.getUsers().add_user(user2)

    ls.setActiveUser(user1)

    book1 = Book(1, 'Time', ['Ajay'])
    book2 = Book(2, 'Man Search for Meaning', ['Some Author'])

    ls.getLibrary().add_book(book2)
    ls.getLibrary().add_book(book1)

    ls.setActiveBooks(book1)
