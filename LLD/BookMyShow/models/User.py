from enum import Enum
from abc import ABC


class UserStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2


class UserRole(Enum):
    ADMIN = 0
    FRONT_OFFICER = 2
    CUSTOMER = 3
    USER = 4


class Address:
    def __init__(self, id, addressline1, city, pincode, state, country):
        self.id = id
        self.addressline1 = addressline1
        self.city = city
        self.pincode = pincode
        self.state = state
        self.country = country


class User(ABC):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def reset_password(self):
        pass

    def book_ticket(self):
        pass

    def cancel_ticket(self):
        pass


class Customer(User):
    def __init__(self, id, name, email, active=UserStatus.ACTIVE, role=UserRole.CUSTOMER):
        self.active = active
        self.role = role
        super(Customer, self).__init__(id, name, email)


class FrontOfficer(User):
    def __init__(self, id, name, email, active=UserStatus.ACTIVE, role=UserRole.FRONT_OFFICER):
        self.active = active
        self.role = role
        super(FrontOfficer, self).__init__(id, name, email)


class Admin(User):
    def __init__(self, id, name, email, active=UserStatus.ACTIVE, role=UserRole.ADMIN):
        self.active = active
        self.role = role
        super(Admin, self).__init__(id, name, email)

    def add_movie(self):
        pass

    def remove_movie(self):
        pass
