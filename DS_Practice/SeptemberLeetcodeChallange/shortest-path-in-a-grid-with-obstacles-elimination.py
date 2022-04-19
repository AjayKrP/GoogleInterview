from queue import Queue

"""
I think this is the simplest of all the solutions that can be possible
Solution:
1. Since it talks about the shortest paths, we immediately think about BFS here.
2. We use the visited array in a different way to keep storing the number of obstacles
that we can still remove after walking through that cell. (Basically BEST remaining K after reaching that cell)
3. Simply traverse the BFS by storing the X, Y, currentLength and currentK remaining in the queue.
4. If you reach the destination index, return the currentLength
5. If you try to access an invalid cell,
or you hit an obstacle but have no K to spend,
or this index X and Y have already been accessed and with a better remaining K than yours, WE SKIP/continue.
6. Push the adjacent indexes into the queue.

TC: O(mn)
SC: O(mn)
"""


class Solution:
    def shortestPath(self, grid, k: int) -> int:
        q = Queue()
        q.put([0, 0, 0, k])
        m, n = len(grid), len(grid[0])
        visited = [[-1 for _ in range(n)] for _ in range(m)]

        while not q.empty():
            t = q.get()
            x, y = t[0], t[1]
            if x < 0 or x >= m or y < 0 or y >= n:
                continue

            if x == m - 1 and y == n - 1:
                return t[2]

            if grid[x][y] == 1:
                if t[3] > 0:
                    t[3] -= 1
                else:
                    continue

            if visited[x][y] != -1 and visited[x][y] >= t[3]:
                continue

            visited[x][y] = t[3]

            q.put([x + 1, y, t[2] + 1, t[3]])
            q.put([x - 1, y, t[2] + 1, t[3]])
            q.put([x, y + 1, t[2] + 1, t[3]])
            q.put([x, y - 1, t[2] + 1, t[3]])

        return -1
