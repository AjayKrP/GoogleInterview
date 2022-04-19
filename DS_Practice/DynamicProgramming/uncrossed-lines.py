class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        self.count = 0

        def helper(nums1, nums2, i, j, x, y):
            if i >= len(nums1):
                return
            if j >= len(nums2):
                return
            if nums1[i] == nums2[j]:
                self.count += 1
                return

            if i <= y or j <= x:
                return
            x = max(x, i)
            y = max(y, j)

            self.max(self.count, helper(nums1, nums2, i + 1, j, x, y) + helper(nums1, nums2, i, j + 1, x, y))

        helper(nums1, nums2, 0, 0, 0, 0)
        return self.count


class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
