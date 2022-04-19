from queue import PriorityQueue


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        pq = PriorityQueue()
        for item in nums:
            pq.put((-1*item, item))

        kth_largest_item = None
        while k and not pq.empty():
            kth_largest_item = pq.get()[1]
            k -= 1
        return kth_largest_item
