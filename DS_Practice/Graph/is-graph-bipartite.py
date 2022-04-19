class Solution1:

    def isBipartite(self, graph) -> bool:
        set1 = set()  # take 2 sets
        set2 = set()

        def isSafe(u, v):
            if (u in set1 and v in set1) or (u in set2 and v in set2):
                return False
            return True

        for u in range(len(graph)):
            for v in graph[u]:
                if not isSafe(u, v):
                    return False
                elif u not in set1 and u not in set2:
                    if v in set1:
                        set2.add(u)
                    else:
                        set1.add(u)
                        set2.add(v)
                elif u in set1:
                    if v in set1:
                        return False
                    if v not in set2:
                        set2.add(v)
                elif u in set2:
                    if v in set2:
                        return False
                    if v not in set1:
                        set1.add(v)
        return True


class Solution:
    def isCycle(self, src, visited, graph):
        if visited[src] == 2:
            return True
        visited[src] = 2
        for v in graph[src]:
            if visited[v] == 1:
                visited[v] = 2
            if self.isCycle(v, visited, graph):
                return True

        return False

    def isBipartite(self, graph) -> bool:
        visited = [0 for _ in range(len(graph))]

        for i in range(len(graph)):
            if self.isCycle(i, visited, graph):
                return False
        return True


def test_bipartite():
    sol = Solution1()
    assert sol.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) == False
    assert sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True
    assert sol.isBipartite([[1], [0, 3], [3], [1, 2]]) == True
    assert sol.isBipartite([[3], [2, 4], [1], [0, 4], [1, 3]]) == True
