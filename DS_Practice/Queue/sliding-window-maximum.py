from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        ans = [nums[dq[0]]]
        for i in range(k, len(nums)):
            if i - dq[0] == k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans
