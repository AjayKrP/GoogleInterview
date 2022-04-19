from queue import PriorityQueue
class Solution:
    def largestSumAfterKNegations(self, nums, k: int) -> int:
        pq = PriorityQueue()
        for item in nums:
            pq.put(item)
        while k:
            front = pq.get()
            pq.put(-1*front)
            k -= 1

        total = 0
        while not pq.empty():
            total += pq.get()
        return total


