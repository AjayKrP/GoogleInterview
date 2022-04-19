from enum import Enum
from abc import ABC

from LLD.CallCenter.models.Call import Call


class Level(Enum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2


class Employee(ABC):
    current_call: Call
    rank: Level

    def __init__(self):
        self.current_call = None
        self.rank = None

    def receive_call(self, call):
        self.current_call = call

    def complete_call(self):
        if not self.current_call:
            raise ValueError('No such call')
        self.current_call = None

    def escalate_and_reassign(self):
        pass

    def is_free(self):
        return self.current_call == None

    def get_rank(self):
        return self.rank

    def assign_new_call(self):
        pass


class Director(Employee):
    def __init__(self):
        self.rank = Level.DIRECTOR
        super().__init__()


class Manager(Employee):
    def __init__(self):
        self.rank = Level.MANAGER
        super().__init__()


class Respondent(Employee):
    def __init__(self):
        self.rank = Level.RESPONDENT
        super().__init__()
