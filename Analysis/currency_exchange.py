from collections import defaultdict
from queue import Queue, PriorityQueue
import math
"""
Currency Exchange
a list of currency relationships with exchange values. (BTC - USD)
find the best exchange rate from currency1 to currency2
"""


# TODO find the best exchange rate from currency1 to currency2

def convert(adj, from_c, to_c):
    queue = Queue()
    queue.put((from_c, 1.0))
    visited = set()
    while not queue.empty():
        node, num = queue.get()
        if node in visited:
            continue
        visited.add(node)
        for items in adj[node]:
            if items[0] == to_c:
                return num * items[1]
            queue.put((items[0], num * items[1]))
    return -1

def getBestCurrencyPath(adj, from_c, to_c):
    pq = PriorityQueue()
    pq.put(from_c)
    while not pq.empty():
        current = pq.get()
        for v in range(adj[current]):
            cost = math.log(current * v[1])
            if v[0] < cost:
                pq.put(v[0], cost)

def getRatio(start, end):
    adj = defaultdict(list)
    for node in data:
        adj[node[0]].append([node[1], node[2]])
        adj[node[1]].append([node[0], 1.0 / node[2]])
    

data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
print(getRatio("AUD", "GBP"))
