class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        mat = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    mat[i][j] = 0
        
        
        for x in edges:
            mat[x[0]][x[1]] = x[2]
            mat[x[1]][x[0]] = x[2]
            
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        
        print(mat)
        res = {}
        for i in range(n):
            cnt = 0
            for j in range(n):
                if mat[i][j] <= distanceThreshold and i != j:
                    cnt += 1
            res[i] = cnt
        
        ans = float('inf')
        key_ans = float('-inf')
        for item in res.items():
            if item[1] <= ans and item[0] > key_ans:
                ans = item[1]
                key_ans = item[0]
        return key_ans
