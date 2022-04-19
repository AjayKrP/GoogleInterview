import math
from queue import PriorityQueue


class Solution:

    def nchoc(self, A, B):
        pq = PriorityQueue()
        for item in B:
            pq.put((-1 * item, item))
        total = 0
        while A:
            curr = pq.get()
            total += curr[1]
            val = math.floor(curr[1] / 2)
            pq.put((-1 * val, val))
            A -= 1
        return int(total%(math.pow(10,9)+7))
