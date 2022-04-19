from collections import deque


class Cache:
    evictionPolicy: EvictionPolicy
    size: int

    def __init__(self, size, evictionPolicy):
        self.size = size
        self.evictionPolicy = evictionPolicy
        self.linkedList = deque()
        self.hashMap = {}

    def clear(self):
        self.linkedList.clear()
        self.hashMap.clear()
        return True

    def getSize(self):
        return self.size

    def getHashMap(self):
        return self.hashMap

    def getLinkedList(self):
        return self.linkedList

    def getEvictionPolicy(self):
        return self.evictionPolicy

