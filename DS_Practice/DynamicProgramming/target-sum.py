class Solution:
    def __init__(self):
        self.count = 0

    def findTargetSumWays(self, nums, target: int) -> int:
        self.hasSum(nums, target, 0, 0)
        return self.count

    def hasSum(self, nums, target, index, total):
        if index == len(nums):
            if total == target:
                self.count += 1
        else:
            self.hasSum(nums, target, index + 1, total + nums[index])
            self.hasSum(nums, target, index + 1, total - nums[index])


sol = Solution()
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
