"""
1. in one city there can be multiple parking lot
2. One parking lot can have multiple entries
3. There can be multiple floors in one parking lot
4. There can be different slots for different type of vehicle
5. There can be parking space for different type of vehicle
6. There can be multiple entries/exit doors
7. There will be time limit for parking vehicle and it will be charged accordingly based on the vehicle type
8. On the entry door receptionist can book ticket
9. Once ticket booked it cant be cancled
10. Customer can pay via credit/debit/cash
11. On exit gate receptionist will verify the ticket and let vehicle exit
12. System should print ticket
"""

from enum import Enum
from abc import ABC, ABCMeta

"""
Vehicle
Customer
System
"""


class VehicleType:
    SMALL = 1
    LARGE = 2
    MEDIUM = 3


class PaymentStatus(Enum):
    SUCCESS = 0
    FAILURE = 1
    PENDING = 2


class Address:
    def __init__(self, street, city, zipcode, state, country):
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.country = country

