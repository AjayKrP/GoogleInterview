from collections import defaultdict


class Solution:

    def detectCycleUtil(self, adj, visited, i):
        if visited[i] == 2:
            return True
        if visited[i] == 1:
            return False
        visited[i] = 2
        for j in range(len(adj[i])):
            if self.detectCycleUtil(adj, visited, adj[i][j]):
                return True
        visited[i] = 1
        return False

    def detectCycle(self, adj, n):
        visited = [0 for _ in range(n)]
        for i in range(n):
            if visited[i] == 0:
                if self.detectCycleUtil(adj, visited, i):
                    return True
        return False

    def dfs(self, adj, i, visited, stack):
        visited[i] = True
        for j in adj[i]:
            if not visited[j]:
                self.dfs(adj, j, visited, stack)
        stack.append(i)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for item in prerequisites:
            adj[item[1]].append(item[0])

        visited = [False for _ in range(numCourses)]

        stack = []

        if self.detectCycle(adj, numCourses):
            return stack

        for i in range(numCourses):
            if not visited[i]:
                self.dfs(adj, i, visited, stack)

        return stack[::-1]
