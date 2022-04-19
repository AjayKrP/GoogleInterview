class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1

        while left <= right:
            tSum = nums[left] + nums[right]
            if tSum == target:
                return [left + 1, right + 1]
            elif tSum < target:
                left += 1
            elif tSum > target:
                right -= 1

        return [-1, -1]