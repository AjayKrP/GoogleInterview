class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dpLow, dpHigh = [1] * n, [1] * n
        ans = 1
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                dpHigh[i] = dpLow[i-1] + 1
            elif arr[i-1] > arr[i]:
                dpLow[i] = dpHigh[i-1] + 1
            ans = max(ans, dpHigh[i], dpLow[i])
        return ans
