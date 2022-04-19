from queue import Queue


class Stack:
    def __init__(self):
        self.__queue1 = Queue()
        self.__queue2 = Queue()
        self.__top = -1

    def push(self, item):
        self.__top += 1
        self.__queue1.put(item)

    def pop(self):
        if not self.isEmpty():
            lastElem = None
            while not self.__queue1.empty():
                lastElem = self.__queue1.get()
                self.__queue2.put(lastElem)
            if lastElem is not None:
                self.__top -= 1
            if self.__top < 0:
                return lastElem
            while not self.__queue2.empty():
                self.__queue1.put(self.__queue2.get())
            return lastElem

    def isEmpty(self):
        return self.__queue1.empty()
