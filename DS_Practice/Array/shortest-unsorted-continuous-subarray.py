class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        tmpArr = sorted(nums)

        startIdx = len(nums) - 1
        endIdx = 0
        for i in range(len(nums)):
            if tmpArr[i] != nums[i]:
                startIdx = min(startIdx, i)
                endIdx = max(endIdx, i)
        return 0 if endIdx - startIdx <= 0 else endIdx - startIdx + 1

