class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N) -> int:
            # base case
            if K == 1: return N
            if N == 0: return 0
            # avoid calculating again
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # Exhaust all possible choices
            for i in range(1, N + 1):
                res = min(res,
                          max(
                                dp(K, N - i), # Not Broken
                                dp(K - 1, i - 1) # Broken
                             ) + 1
                      )
            # Record into memo
            memo[(K, N)] = res
            return res

        return dp(K, N)