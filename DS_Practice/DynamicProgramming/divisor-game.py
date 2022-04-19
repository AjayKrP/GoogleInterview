class Solution:
    def divisorGame(self, n: int) -> bool:
        def helper(n, curr):
            if n == 0:
                return curr % 2 == 1
            return helper(n-1, curr + 1)
        
        return helper(n, 1)
