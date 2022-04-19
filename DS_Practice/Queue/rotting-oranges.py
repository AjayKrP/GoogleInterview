from queue import Queue
class Solution:
    def inRange(self, cord, m, n):
        x, y = cord
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return True
        
    def orangesRotting(self, grid) -> int:
        q = Queue()
        m, n = len(grid), len(grid[0])
        cnt  = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put([i, j])
                elif grid[i][j] == 1:
                    cnt += 1
                
        time = 0
        dir_ = [[1,0], [0, 1], [-1, 0], [0, -1]]
        while not q.empty() and cnt:
            qL = q.qsize()
            
            while qL:
                t = q.get()
                for d in dir_:
                    x, y = t[0] + d[0], t[1] + d[1]
                    if (self.inRange([x, y], m, n)):
                        if (grid[x][y] == 1):
                            q.put([x, y])
                            grid[x][y] = 2
                            cnt -= 1
                print(qL)
                qL -= 1
            time += 1
        return time if cnt == 0 else -1

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
