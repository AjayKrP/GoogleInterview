from queue import PriorityQueue


class Solution:
    def mergeStones(self, stones, k: int) -> int:
        q = PriorityQueue()
        for item in stones:
            q.put(item)
        total = 0
        while q.qsize() > 1:
            item1 = q.get()
            item2 = q.get()
            cost = item1 + item2
            total += cost
            q.put(cost)
        return total if total > 0 else -1
