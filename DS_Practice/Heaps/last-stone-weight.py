from queue import PriorityQueue


class Solution:
    def lastStoneWeight(self, stones) -> int:
        pq = PriorityQueue()
        for item in stones:
            pq.put((-1*item, item))
        while pq.qsize() > 1:
            item1 = pq.get()[1]
            item2 = pq.get()[1]
            if item2 != item1:
                diff = abs(item2 - item1)
                pq.put((-1*diff, diff))
        return pq.get()[1] if pq.qsize() > 0 else 0


sol = Solution()
print(sol.lastStoneWeight([2, 2]))
