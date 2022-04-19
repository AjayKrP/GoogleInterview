class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mineSet = set((x, y) for x, y in mines)
        
        left = [[0]*n for _ in range(n)]
        right = [[0]*n for _ in range(n)]
        up = [[0]*n for _ in range(n)]
        down = [[0]*n for _ in range(n)]
        
        
        for i in range(n):
            for j in range(n):
                if (i, j) not in mineSet:
                    if i == 0 or j == 0:
                        up[i][j] = left[i][j] = 1
                    else:
                        up[i][j] = up[i][j-1] + 1
                        left[i][j] = left[i-1][j] + 1
                    
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mineSet:
                    if i == n-1 or j == n-1:
                        down[i][j] = right[i][j] = 1
                    else:
                        down[i][j] = down[i][j+1] + 1
                        right[i][j] = right[i+1][j] + 1
        
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                ans = max(ans,min(down[i][j], left[i][j], right[i][j], up[i][j] ))
        
        return ans
                
        
                
