from collections import defaultdict


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Node:
    rank = 0
    parent = -1


class Graph:
    def __init__(self):
        self.adj = []

    class UnionFind:
        def path_compression_cycle_detection(self):
            pass

        @staticmethod
        def union_by_rank(dsuf, fromP, toP):
            if dsuf[fromP].rank > dsuf[toP].rank:
                dsuf[toP].parent = fromP
            elif dsuf[fromP].rank < dsuf[toP].rank:
                dsuf[fromP].parent = toP
            else:
                dsuf[fromP].parent = toP
                dsuf[toP].rank += 1

        def find(self, dsuf, curr):
            if dsuf[curr].parent == -1:
                return curr
            dsuf[curr].parent = self.find(dsuf, dsuf[curr].parent)  # path compression
            return dsuf[curr].parent

        def union(self, u, v):
            pass

    def _add_edge(self, u, v, w):
        self.adj.append(Edge(u, v, w))

    @staticmethod
    def krushkal_algorithm(dsuf, adj, V, E):
        # sort the edge list according to weight
        mst = []
        i, j = 0, 0
        uf = Graph.UnionFind()
        while i < V - 1 and j < E:
            fromP = uf.find(dsuf, adj[j].src)
            toP = uf.find(dsuf, adj[j].dst)
            if fromP == toP:
                j += 1
                continue

            uf.union_by_rank(dsuf, fromP, toP)
            mst.append(adj[j])
            i += 1

        def test_krushkal():
            E = 6
            dsuf = [Node for _ in range(E)]

            adj = []
