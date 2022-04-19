class Solution:

    def allPathsSourceTarget(self, graph):
        def dfs(sv, dv, path, result):
            if sv == dv:
                result.append(path)
            for nei in graph[sv]:
                dfs(nei, dv, path+[nei], result)
            return result
        return dfs(0, len(graph)-1, [0], [])


sol = Solution()
print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))