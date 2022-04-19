class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        even = 0
        odd = 1
        for i in range(n):
            if i%2 == 0 and nums[i] %2 != 0:
                even = i
                while even < n:
                    if nums[even]%2 == 0:
                        nums[i], nums[even] = nums[even], nums[i]
                        break
                    even += 1
            elif i%2 != 0 and nums[i] %2 == 0:
                odd = i
                while odd < n:
                    if nums[odd]%2 != 0:
                        nums[i], nums[odd] = nums[odd], nums[i]
                        break
                    odd += 1
            
        return nums
            
