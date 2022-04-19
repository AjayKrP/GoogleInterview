from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int):
        dq = deque()
        p = [0]
        for x in nums:
            p.append(p[-1]+x)
        index_diff = float('inf')
        for i in range(len(p)):
            while dq and p[dq[-1]] >= p[i]:
                dq.pop()

            while dq and p[i] - p[dq[0]] >= k:
                index_diff = min(index_diff, i - dq.popleft())

            dq.append(i)

        return index_diff