from queue import PriorityQueue
import math as m


class Solution:
    def kClosest(self, points, k: int):
        pq = PriorityQueue()

        def dist(point):
            return m.sqrt(point[0] ** 2 + point[1] ** 2)

        for point in points:
            pq.put((dist(point), point))
        result = []
        while k:
            front = pq.get()
            result.append(front[1])
            k -= 1

        return result
