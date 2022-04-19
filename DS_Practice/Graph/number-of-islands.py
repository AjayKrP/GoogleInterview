from queue import Queue


class Solution:
    def numIslands(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        iland = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            for j in range(n):
                print(i, j)
                if grid[i][j] == '1' and not visited[i][j]:
                    q = Queue()
                    q.put((i, j))
                    iland += 1
                    visited[i][j] = True
                    while not q.empty():
                        front = q.get()
                        for k in range(4):
                            cx = directions[k][0] + front[0]
                            cy = directions[k][1] + front[1]
                            if 0 <= cx < m and 0 <= cy < n and not visited[cx][cy] and grid[cx][cy] == '1':
                                visited[cx][cy] = True
                                q.put((cx, cy))
        return iland
