import math


class Solution:
    def is_perfect_square(self, x):
        if x >= 0:
            s = int(math.sqrt(x))
            return s * s == x
        return False

    def numSquarefulPerms(self, nums) -> int:
        res = []
        def helper(l, r, res):
            if l == r:
                for i in range(r):
                    if not self.is_perfect_square(nums[i] + nums[i + 1]):
                        return
                if nums not in res:
                    res.append(nums[:])
                return
            for i in range(l, r + 1):
                nums[i], nums[l] = nums[l], nums[i]
                helper(l + 1, r, res)
                nums[i], nums[l] = nums[l], nums[i]
            return res

        return len(helper(0, len(nums) - 1, []))


sol = Solution()
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
arr = [1, 17, 8]
print(sol.numSquarefulPerms(arr))
