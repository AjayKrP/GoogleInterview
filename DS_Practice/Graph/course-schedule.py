from collections import defaultdict


class Solution1:
    def detectCycle(self, src, adj, visited):
        if visited[src]:
            return True
        visited[src] = True
        for v in adj[src]:
            if self.detectCycle(v, adj, visited):
                return True
        visited[src] = False
        return False

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)

        visited = [False for _ in range(numCourses)]

        for u in range(numCourses):
            visited[u] = True
            for v in adj[u]:
                if self.detectCycle(v, adj, visited):
                    return True
            visited[u] = False
        return False


class Solution:
    def detectCycle(self, src, adj, visited):
        if visited[src] == 2:
            return True
        visited[src] = 2
        for v in adj[src]:
            if visited[v] != 1 and self.detectCycle(v, adj, visited):
                return True
        visited[src] = 1
        return False

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)

        visited = [0 for _ in range(numCourses)]

        for u in range(numCourses):
            for v in adj[u]:
                if self.detectCycle(v, adj, visited):
                    return False
        return True
