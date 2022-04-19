from queue import PriorityQueue


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        pq = PriorityQueue()
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(n1):
            for j in range(n2):
                pq.put((nums1[i]+nums2[j], [nums1[i], nums2[j]]))
        res = []
        while k:
            res.append(pq.get()[1])
            k -= 1
        return res

