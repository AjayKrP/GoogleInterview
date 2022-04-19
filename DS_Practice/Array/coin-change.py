class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                sub = helper(n - coin)
                if sub == -1:
                    continue
                res = min(res, 1 + sub)
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return helper(amount)
