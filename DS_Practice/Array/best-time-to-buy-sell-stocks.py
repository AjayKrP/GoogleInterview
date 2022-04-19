class Solution:
    def maxProfit(self, prices) -> int:
        gmax = float('-inf')
        currMax = 0
        for i in range(1, len(prices)):
            currMax += prices[i] - prices[i-1]
            currMax = max(0, currMax)
            gmax = max(gmax, currMax)
        return gmax

