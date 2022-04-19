from enum import Enum
from abc import ABC


class MovieStatus(Enum):
    ACTIVE = 0
    EXPIRED = 1
    PENDING = 2


class Movie:
    def __init__(self, id, name, status=MovieStatus.PENDING):
        self.__id = id
        self.name = name
        self.status = status

    def getId(self):
        return self.__id


