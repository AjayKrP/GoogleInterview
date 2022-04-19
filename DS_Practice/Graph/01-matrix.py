from queue import Queue


class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])

        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        q = Queue()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.put((i, j))

        distances = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while not q.empty():
            front = q.get()
            for k in range(4):
                cx = front[0] + distances[k][0]
                cy = front[1] + distances[k][1]
                if 0 <= cx < m and 0 <= cy < n and dist[cx][cy] > dist[front[0]][front[1]] + 1:
                    dist[cx][cy] = dist[front[0]][front[1]] + 1
                    q.put((cx, cy))
        return dist
