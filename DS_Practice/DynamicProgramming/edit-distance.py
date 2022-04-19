class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dp(i, j):
            if i < 0: return j + 1
            if j < 0: return i + 1
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)  # skip
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,  # insert
                    dp(i - 1, j - 1) + 1,  # replace
                    dp(i - 1, j) + 1)  # delete
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # base case
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        # from the bottom up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        return dp[m][n]
