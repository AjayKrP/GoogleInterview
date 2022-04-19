class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1):
            if nums[i] == 0:
                curr = i + 1
                while curr < len(nums) and nums[curr] == 0:
                    curr += 1
                if curr < len(nums):
                    nums[i], nums[curr] = nums[curr], nums[i]


sol = Solution()
print(sol.moveZeroes([0, 1, 0, 2, 0, 0, 0, 2, 4, 0, 2]))


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1
        while cnt < len(nums):
            nums[cnt] = 0
            cnt += 1
