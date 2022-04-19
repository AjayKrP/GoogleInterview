class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        @cache
        def dp(i, j):
            if i == j-1:
                return 0
            return cuts[j]-cuts[i] + min(dp(i, k) + dp(k, j) for k in range(i+1, j))
        return dp(0, len(cuts)-1)