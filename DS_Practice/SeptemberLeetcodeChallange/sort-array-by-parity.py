class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = n-1
        for i in range(n-1, -1, -1):
            if nums[i] % 2 != 0:
                nums[odd], nums[i] = nums[i], nums[odd]
                odd -= 1
                
        return nums
                
        
