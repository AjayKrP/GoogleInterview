from collections import defaultdict
from queue import Queue


class Solution(object):
    def distanceK(self, root, target, K):
        ans = []
        graph = defaultdict(list)
        visited = {}

        def buildGraph(root, parent):
            if not root:
                return
            visited[root.val] = False
            if not graph[root.val]:
                if parent:
                    graph[root.val].append(parent.val)
                    graph[parent.val].append(root.val)

                buildGraph(root.left, root)
                buildGraph(root.right, root)

        def bfs(target, k):
            q = Queue()
            depth = 0
            if k == 0:
                ans.append(target.val)
                return
            q.put(target.val)
            while not q.empty():
                depth += 1
                qsize = q.qsize()
                for _ in range(qsize):
                    curr = q.get()
                    visited[curr] = True

                    for neighbour in graph[curr]:
                        if not visited[neighbour]:
                            if depth == k:
                                ans.append(neighbour)
                            else:
                                q.put(neighbour)
                if depth == k:
                    return

        buildGraph(root, None)
        bfs(target, K)
        return ans
        # Return distance from node to target if exists, else -1

        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans


"""
https://afteracademy.com/blog/all-nodes-distance-k-in-binary-tree#:~:text=Percolate%20Distance,-The%20problem%20can&text=If%20the%20node%20is%20not,or%20in%20the%20right%20subtree.&text=It%20means%20that%20any%20nodes,with%20a%20depth%2Dfirst%20search.
"""