class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result_num = 0
        for i in range(len(nums)):
            result_num ^= nums[i]

        return result_num

