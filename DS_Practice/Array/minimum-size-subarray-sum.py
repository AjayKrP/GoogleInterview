class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # preSum = [0 for _ in range(n+1)]
        # for i in range(n):
        #     preSum[i+1] = preSum[i] + nums[i]
            
            
        minLen = float('inf')
        # for i in range(1, n+1):
        #     for j in range(i, n+1):
        #         tmp =  preSum[j] - preSum[i] + nums[i-1]
        #         if tmp >=  target:
        #             minLen = min(minLen, (j-i+1))
        #             break
        
        tmp = 0
        left = 0
        for i in range(n):
            tmp += nums[i]
            while tmp >= target:
                minLen = min(minLen, (i + 1 - left))
                tmp -= nums[left]
                left += 1
        
        return minLen if minLen <= 10**5 else 0
        
