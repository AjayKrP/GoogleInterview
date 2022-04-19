class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def helper(mat, i, j, m, n, dist):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if mat[i][j] == 0:
                return 0

            return min(helper(mat, i+1, j, m, n, dist) + 1, helper(mat, i-1, j, m, n, dist) + 1, helper(mat, i, j-1, m, n, dist) + 1, helper(mat, i, j+1, m, n, dist) + 1)
        
        m = len(mat)
        n = len(mat[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    result[i][j] = helper(mat, i, j,m, n, 0)
        return result
    
    
        
                    
        
