class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            ans[i] = 0 if len(stack) == 0 else abs(stack[-1] - i)
            stack.append(i)
        return ans
