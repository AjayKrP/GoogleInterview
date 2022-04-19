from enum import Enum
from abc import ABC


class EvictionPolicy(ABC):
    LRU = 0
    LFU = 1


class Cache:
    def __init__(self, size, evictionPolicy=EvictionPolicy.LRU):
        self.__size = size
        self.__evictionPolicy = evictionPolicy
        self.__linkedList = []
        self.__hashMap = {}

    def clear(self):
        self.__linkedList = []
        self.__hashMap = {}
        self.__evictionPolicy = EvictionPolicy.LRU

    def getSize(self):
        return self.__size

    def getLinkedList(self):
        return self.__linkedList

    def getHashMap(self):
        return self.__hashMap

    def getEvictionPolicy(self):
        return self.__evictionPolicy


class CacheDao:
    __instance = None
    __cache = None

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if CacheDao.__instance is None:
            CacheDao.__instance = CacheDao()
        return CacheDao.__instance

    def createCache(self, size, evictionPolicy):
        if self.__cache is None:
            self.__cache = Cache(size, evictionPolicy)
        return self.__cache

    def get(self, obj):
        result = self.__cache.getHashMap().get(obj)
        if result is None:
            return None
        self.__cache.getLinkedList().remove(obj)
        self.__cache.getLinkedList().insert(0, obj)

        return result

    def put(self, key, val):
        if self.__cache.getSize() == len(self.__cache.getLinkedList()):
            last = self.__cache.getLinkedList().pop()
            self.__cache.getHashMap().pop(last)

        if key in self.__cache.getHashMap():
            self.__cache.getLinkedList().remove(key)
        self.__cache.getLinkedList().insert(0, key)
        self.__cache.getHashMap().setdefault(key, val)

        return True

    def clear(self):
        self.__cache.clear()

    def delete(self, key):
        if len(self.__cache.getLinkedList()) == 0:
            return False
        self.__cache.getLinkedList().remove(key)
        self.__cache.getHashMap().pop(key)

    def getSize(self):
        return len(self.__cache.getLinkedList())


class CacheService:
    __cacheService = None

    def __init__(self):
        self.__cacheDao = CacheDao.getInstance()

    @staticmethod
    def getInstance():
        if CacheService.__cacheService is None:
            CacheService.__cacheService = CacheService()
        return CacheService.__cacheService

    def init(self, size, evictionPolicy):
        return self.__cacheDao.createCache(size, evictionPolicy)

    def put(self, key, val):
        self.__cacheDao.put(key, val)

    def get(self, key):
        return self.__cacheDao.get(key)

    def clear(self, key):
        return self.__cacheDao.clear()

    def delete(self, ky):
        return self.__cacheDao.delete(ky)

    def getSize(self):
        return self.__cacheDao.getSize()


class DriverClass:
    cacheService = CacheService.getInstance()
    cache = cacheService.init(10, EvictionPolicy.LRU)
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    cacheService.put("hey", "First Object")
    print(cacheService.get("hey"))
    print(cacheService.getSize())
