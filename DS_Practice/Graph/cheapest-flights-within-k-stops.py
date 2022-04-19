import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        w_g = collections.defaultdict(list)
        for a, b, p in flights:
            w_g[a].append((b, p))
        heap = [(0, src, k)]
        while len(heap) != 0:
            cost, cur_node, n_stop = heapq.heappop(heap)
            if cur_node == dst:
                return cost
            if n_stop >= 0:
                for nei_node, p in w_g[cur_node]:
                    heapq.heappush(heap, (cost + p, nei_node, n_stop - 1))
        return -1
