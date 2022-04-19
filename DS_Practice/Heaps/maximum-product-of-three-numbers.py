import heapq


class Solution:
    def maximumProduct(self, nums) -> int:
        nlargest = heapq.nlargest(3, nums)
        nsmallest = heapq.nsmallest(2, nums)

        return max(nlargest[0] * nlargest[1] * nlargest[2], nlargest[0] * nsmallest[0] * nsmallest[1])
