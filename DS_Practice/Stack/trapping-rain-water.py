class Solution:
    def trap(self, height) -> int:
        stack = []
        ans = 0
        for i in range(len(height)-1, -1, -1):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                dist = stack[-1] - i - 1
                print(f'dist: {dist}')
                bh = min(height[i], height[stack[-1]]) - height[top]
                print(f'bh: {bh}')
                ans += dist*bh
                print(f'ans: {ans}')
            
            stack.append(i)
        
        return ans
        
