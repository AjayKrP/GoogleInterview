class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
                continue
            left += 1
            nums[left] = nums[right]
            right += 1
        return left + 1

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i-1]
                k += 1
        return k+1
