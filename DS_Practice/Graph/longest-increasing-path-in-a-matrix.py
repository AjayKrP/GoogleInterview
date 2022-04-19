class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        result = 0
        if not matrix:
            return result

        N, M = len(matrix), len(matrix[0])
        dp = [[None] * M for _ in range(N)]
        for row in range(N):
            for col in range(M):
                # note, no visited set is needed, if we only step on increasing cells.
                # this guarantees we won't step on same cell twice.
                result = max(result, self.dfs_increase(matrix, row, col, 1, dp))
        return result

    def dfs_increase(self, matrix, r, c, plen, dp):
        if dp[r][c]:
            return dp[r][c]

        directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        steps = [
            (x, y)
            for (x, y) in directions
            if (
                    0 <= x < len(matrix) and
                    0 <= y < len(matrix[0]) and
                    matrix[x][y] > matrix[r][c]
            )
        ]
        result = plen
        for (x, y) in steps:
            result = max(result, 1 + self.dfs_increase(matrix, x, y, plen, dp))

        dp[r][c] = result
        return dp[r][c]
