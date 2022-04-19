class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        maxSqLen = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxSqLen = max(maxSqLen, dp[i][j])

        return maxSqLen * maxSqLen
