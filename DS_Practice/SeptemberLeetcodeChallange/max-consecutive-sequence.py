class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        prev = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                res = max(count, res)
        return res
                
        
