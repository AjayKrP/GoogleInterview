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


class Solution1:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)

        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        stack = []
        for i in range(n):

            # find the nearest element on left less than heights[i]
            # by popping item off the stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # store the current top of the stack
            left[i] = 0 if not stack else stack[-1] + 1

            stack.append(i)

        # find right
        stack = []
        for i in reversed(range(n)):
            # find the nearest element on right less than heights[i]
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # store the current top of the stack
            right[i] = n - 1 if not stack else stack[-1] - 1

            stack.append(i)

        # find max rectangle
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            max_area = max(max_area, heights[i] * width)

        return max_area