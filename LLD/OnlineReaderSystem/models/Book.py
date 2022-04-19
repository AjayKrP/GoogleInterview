class Book:
    def __init__(self, id, name, authors: object):
        self.id = id
        self.__name = name
        self.__authors = authors

    def get_id(self):
        return self.id

    def get_book_name(self):
        return self.__name

    def get_book_authors(self):
        return self.__authors

    def __str__(self):
        return f'Current Book: {self.__name}'