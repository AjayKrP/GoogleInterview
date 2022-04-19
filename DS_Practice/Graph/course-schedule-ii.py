from queue import Queue
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        inDegree = [0] * numCourses
        adj = defaultdict(list)
        q = Queue()
        for u, v in prerequisites:
            adj[u].append(v)
            inDegree[v] += 1
        for i, val in enumerate(inDegree):
            if val == 0:
                q.put(i)
        result = []
        count = 0
        while not q.empty():
            front = q.get()
            result.append(front)
            for child in adj[front]:
                if inDegree[child] > 0:
                    inDegree[child] -= 1
                if inDegree[child] == 0:
                    q.put(child)
            count += 1
        return result[::-1] if count == numCourses else []


sol = Solution()
print(sol.findOrder(2, [[1, 0]]))
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(sol.findOrder(1, []))
print(sol.findOrder(3, [[0, 2], [1, 2], [2, 0]]))
