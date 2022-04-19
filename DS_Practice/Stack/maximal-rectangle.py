class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights) + 1):
            while len(stack) and (i == len(heights) or heights[i] < heights[stack[-1]]):
                currHeight = heights[stack.pop()]

                if len(stack) > 0:
                    currWidth = i - stack[-1] - 1
                else:
                    currWidth = i

                maxArea = max(maxArea, currHeight * currWidth)
            stack.append(i)
        return maxArea

    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return -1
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])

        dp = matrix[0]
        max_ = 0
        for i in range(m):
            if i == 0:
                max_ = max(max_, self.largestRectangleArea(dp))
                continue
            for j in range(n):
                if matrix[i][j] != 0:
                    dp[j] = dp[j] + matrix[i][j]
                else:
                    dp[j] = 0
            max_ = max(max_, self.largestRectangleArea(dp))
        return max_