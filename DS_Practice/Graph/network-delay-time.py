# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         """
#         Bellmanford Algorithm
#         """
#         dist = [float('inf')]*n
#
#         dist[k-1] = 0
#
#         print(times)
#         for _ in range(n):
#             for time in times:
#                 if dist[time[0]-1] + time[2] < dist[time[1]-1]:
#                     dist[time[1]-1] = dist[time[0]-1] + time[2]
#
#
#         return max(dist) if max(dist) < float('inf') else -1
#
#
#
#

# Bellman Ford
from queue import PriorityQueue


class Solution1:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        dist[k - 1] = 0
        visited = [False for _ in range(n)]
        for _ in range(n):
            for time in times:
                if dist[time[0] - 1] + time[2] < dist[time[1] - 1]:
                    dist[time[1] - 1] = dist[time[0] - 1] + time[2]

        return max(dist) if max(dist) < float('inf') else -1


from queue import PriorityQueue
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, n: int, k: int):
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0
        graph = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for time in times:
            graph[time[0]][time[1]] = time[2]
        q = PriorityQueue()
        q.put(k)
        while not q.empty():
            u = q.get()
            for v in graph[u]:
                if graph[u][v] != -1 and graph[u][v] + dist[u] < dist[v]:
                    dist[v] = graph[u][v] + dist[u]
                    q.put(v)
        print(dist)


sol = Solution()
print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
