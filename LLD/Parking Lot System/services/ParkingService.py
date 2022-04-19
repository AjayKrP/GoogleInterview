import threading


class ParkingService:
    def __init__(self):
        self.__lock = threading.Lock()

    def test(self):
        self.__lock.acquire()
        ## your code here
        self.__lock.release()