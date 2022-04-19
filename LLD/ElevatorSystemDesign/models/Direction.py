from enum import Enum
from heapq import *


class Direction(Enum):
    UP = 0
    DOWN = 1
    IDLE = 2


class RequestType(Enum):
    EXTERNAL = 0
    INTERNAL = 1


class Request:
    def __init__(self, origin, target, typeR, direction):
        self.target = target
        self.typeR = typeR
        self.origin = origin
        self.direction = direction

