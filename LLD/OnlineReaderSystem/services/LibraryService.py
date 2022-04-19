from OnlineReaderSystem.models.Book import Book


class LibraryService:
    def __init__(self):
        self.__books = {}

    def add_book(self, book):
        if book.id not in self.__books.keys():
            self.__books[book.id] = book
            return True

        raise  ValueError('Book Already exists!')

    def remove_book(self, bookId):
        for idx, buk in enumerate(self.__books.keys()):
            if bookId == buk.id:
                del self.__books[idx]
                return True
        raise ValueError('user does not exists!')