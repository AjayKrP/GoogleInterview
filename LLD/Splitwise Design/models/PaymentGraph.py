from collections import defaultdict
from models import *

class PaymentGraph:
    def __init__(self):
        self.graph = list()  # Map<User, Map<User, Amount>>
