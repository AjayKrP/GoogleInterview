from collections import deque


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, size):
        self.size = size
        self.cache = []
        self.map = {}

    def get(self, key):
        if key not in self.map:
            return -1
        val = self.map[key].val
        self.put(key, val)
        return val

    def put(self, key, val):
        x = Node(key, val)
        print(self.cache)
        if key in self.map:
            self.cache.remove(self.map.get(key))
            self.cache.insert(0, x)
            self.map[key] = x
        else:
            if self.size == len(self.cache):
                last = self.cache.pop()
                del self.map[last.key]

            self.cache.insert(0, x)
            self.map[key] = x


lru = LRUCache(5)


def test_lru_cache():
    assert lru.get(1) == -1
    lru.put(1, 100)
    lru.put(4, 100)
    lru.put(3, 100)
    lru.put(8, 100)
    lru.put(2, 100)
    lru.put(5, 100)

    assert lru.get(1) == 2
