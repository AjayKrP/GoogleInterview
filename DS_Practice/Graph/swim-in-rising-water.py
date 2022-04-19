from queue import PriorityQueue


class Solution:
    def swimInWater(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        pq = PriorityQueue()
        visited = [[False for _ in range(n)] for _ in range(m)]
        pq.put((grid[0][0], 0, 0))
        visited[0][0] = True
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while not pq.empty():
            front = pq.get()
            if front[1] == m-1 and front[2] == n-1:
                return front[0]
            for d in direction:
                cx = d[0] + front[1]
                cy = d[1] + front[2]
                if cx < 0 or cx >= m or cy < 0 or cy >= n or visited[cx][cy]:
                    continue
                pq.put((max(grid[cx][cy], front[0]), cx, cy))
                visited[cx][cy] = True
        return 0