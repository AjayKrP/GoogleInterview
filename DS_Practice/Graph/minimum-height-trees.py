from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            # adj[v].append(u)

        print(adj)
        visited = {}
        res = []

        def dfs(c, l, ans):
            if c in visited:
                return visited[c]
            visited[c] = True
            for u in adj[c]:
                if dfs(u, l + 1, ans):
                    return True
            visited[c] = False
            if ans >= l:
                print(l)
                ans = l
                res.append(c)
            return False

        for x in range(len(edges)):
            if dfs(x, 0, float('inf')):
                return res
        return res


sol = Solution()
print(sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
