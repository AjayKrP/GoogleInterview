# from queue import PriorityQueue
#
# class KthLargest:
#
#     def __init__(self, k: int, nums):
#         self.k = k
#         self.pq  = PriorityQueue()
#         for num in nums:
#             self.pq.put((num, num))
#
#     def add(self, val: int) -> int:
#         self.pq.put((val, val))
#         curr = 0
#         tmp = PriorityQueue()
#         while self.pq.qsize() > self.k:
#             curr = self.pq.get()
#             tmp.put(curr)
#         while tmp.qsize() > 0:
#             self.pq.put(tmp.get())
#         return curr[0]
#
# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)

import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]