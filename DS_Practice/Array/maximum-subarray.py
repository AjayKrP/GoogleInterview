class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax = float('-inf')
        tsum = 0
        for i in range(len(nums)):
            tsum += nums[i]
            gmax = max(tsum, gmax)
            if tsum < 0:
                tsum = 0

        return gmax
