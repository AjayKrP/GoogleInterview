from cachetools.func import lru_cache


def swap_value(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Input type is not a int')
    a = a + b
    b = a - b
    a = a - b
    return a, b


def test_swap():
    assert swap_value(2, 3) == (3, 2)
    assert swap_value(-5, 2) == (2, -5)
    assert swap_value(-9, -10) == (-10, -9)


def prefix_sum(arr, target):
    n = len(arr)
    preSum = [0] * (n + 1)

    for i in range(n):
        preSum[i + 1] = preSum[i] + arr[i]
    ans = 0

    for i in range(1, n + 1):
        for j in range(i):
            if preSum[i] - preSum[j] == target:
                ans += 1
    return ans


def test_prefix_sum():
    assert prefix_sum([1, 1, 1], 2) == 2


def interval_merging(arr):
    if not arr:
        return []
    arr.sort(key=lambda x: x[0])
    res = list()
    res.append(arr[0])

    for i in range(1, len(arr)):
        curr = arr[i]
        last = res[-1]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res


def test_interval_merging():
    assert interval_merging([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def moore_majority_voting_algorithm():
    pass


# Max Sum subarray
def kadanes_algorithm(arr):
    max_so_far = float('-inf')
    curr_max = 0
    for i in range(len(arr)):
        curr_max += arr[i]
        if curr_max > max_so_far:
            max_so_far = curr_max
        if curr_max < 0:
            curr_max = 0
    return max_so_far


def test_kadanes_algorithm():
    assert kadanes_algorithm([-2, -3, 4, -1, -2, 1, 5, -3]) == 7


def bfs_graph():
    pass


from queue import Queue


# BFS & Flood Fill
def floodFill(image, sr: int, sc: int, newColor: int):
    m = len(image)
    n = len(image[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = Queue()
    q.put((sr, sc))
    currColor = image[sr][sc]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited[sr][sc] = True
    image[sr][sc] = newColor
    while not q.empty():
        front = q.get()
        for i in range(4):
            cx = front[0] + directions[i][0]
            cy = front[1] + directions[i][1]

            if 0 <= cx < m and 0 <= cy < n:
                if not visited[cx][cy] and image[cx][cy] == currColor:
                    image[cx][cy] = newColor
                    q.put((cx, cy))
                    visited[cx][cy] = True
    return image


# https://leetcode.com/problems/island-perimeter/submissions/
def islandPerimeter(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = Queue()
    sr, sc = 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                sr, sc = i, j
                break
    q.put((sr, sc))
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited[sr][sc] = True
    area = 0
    while not q.empty():
        front = q.get()
        for i in range(4):
            cx = front[0] + directions[i][0]
            cy = front[1] + directions[i][1]
            if 0 <= cx < m and 0 <= cy < n:
                if not visited[cx][cy] and grid[cx][cy] == 1:
                    visited[cx][cy] = True
                    q.put((cx, cy))
                elif grid[cx][cy] == 0:
                    area += 1
            else:
                area += 1
    return area


def colorBorder(self, grid, row: int, col: int, color: int):
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = Queue()
    q.put((row, col))
    currColor = grid[row][col]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited[row][col] = True
    grid[row][col] = color
    while not q.empty():
        front = q.get()
        for i in range(4):
            cx = front[0] + directions[i][0]
            cy = front[1] + directions[i][1]

            if 0 <= cx < m and 0 <= cy < n:
                if not visited[cx][cy] and grid[cx][cy] == currColor:
                    grid[cx][cy] = color
                    q.put((cx, cy))
                    visited[cx][cy] = True
    return grid


def prefix_sum_in_matrix(self, mat):
    m, n = len(mat), len(mat[0])
    colM = [[0 for _ in range(n)] for _ in range(m)]
    rowM = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        rowM[i][0] = mat[i][0]
        for j in range(1, n):
            rowM[i][j] = rowM[i][j - 1] + mat[i][j]

    for j in range(n):
        colM[0][j] = mat[0][j]
        for i in range(1, m):
            colM[i][j] = colM[i - 1][j] + mat[i][j]

    for i in range(m):
        for j in range(n):
            mat[i][j] = min(rowM[i][j], colM[i][j])
    return mat


from queue import Queue


# https://leetcode.com/problems/01-matrix/submissions/
def updateMatrix(self, mat):
    q = Queue()

    m = len(mat)
    n = len(mat[0])
    if m == 0:
        return mat

    dist = [[float('inf') for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.put([i, j])

    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while not q.empty():
        front = q.get()
        for i in range(4):
            cr = front[0] + d[i][0]
            cc = front[1] + d[i][1]

            if 0 <= cr < m and 0 <= cc < n:
                if dist[cr][cc] > dist[front[0]][front[1]] + 1:
                    dist[cr][cc] = dist[front[0]][front[1]] + 1
                    q.put([cr, cc])
    return dist


def orangesRotting(self, grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = Queue()
    rottenOrange = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rottenOrange.append([i, j])
    time = 0
    for row, col in rottenOrange:
        if not visited[row][col]:
            q.put((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited[row][col] = True
            while not q.empty():
                front = q.get()
                for i in range(4):
                    cx = front[0] + directions[i][0]
                    cy = front[1] + directions[i][1]

                    if 0 <= cx < m and 0 <= cy < n:
                        if not visited[cx][cy] and grid[cx][cy] == 1:
                            grid[cx][cy] = 2
                            q.put((cx, cy))
                            visited[cx][cy] = True
                time += 1
        return time


# https://leetcode.com/problems/coin-change/submissions/
def coinChange(self, coins, amount: int) -> int:
    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for coin in coins:
            sub = helper(n - coin)
            if sub == -1:
                continue
            res = min(res, 1 + sub)
        memo[n] = res if res != float('inf') else -1
        return memo[n]

    return helper(amount)


# https://leetcode.com/problems/minimum-cost-for-tickets/

def allPathsSourceTarget(self, graph):
    stack = []
    stack.append(0)
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while stack:
        curr = stack[-1]
        for i in range(len(directions)):
            cx = curr


# BST to Balanced BST

# https://leetcode.com/problems/balance-a-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root):

        def getNodes(root, nodes):
            if root is None:
                return
            getNodes(root.left, nodes)
            nodes.append(root.val)
            getNodes(root.right, nodes)

        def makeTree(nodes, start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(nodes[start])

            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = makeTree(nodes, start, mid - 1)
            node.right = makeTree(nodes, mid + 1, end)
            return node

        nodes = []
        getNodes(root, nodes)
        return makeTree(nodes, 0, len(nodes) - 1)


# Dynamic Programming
import sys


class Solution:
    def minDistance(self, houses, k: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            if i == n and k == 0:
                return 0
            if i == n or k == 0:
                return sys.maxsize
            ans = sys.maxsize
            for j in range(i, n):
                ans = min(ans, dp(j + 1, k - 1) + dist[i][j])
            return ans

        n = len(houses)
        houses.sort()
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = houses[(i + j) // 2]
                for h in range(i, j + 1):
                    dist[i][j] += abs(mid - houses[h])
        return dp(0, k)


from collections import defaultdict
from queue import Queue


class GraphAdjList:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def build_graph(self, graph):
        for u, v in graph:
            self.adj[u].append(v)
            self.adj[v].append(u)

    def dfs(self, visited, src):
        print(src)
        visited[src] = True
        for v in self.adj[src]:
            if not visited[v]:
                self.dfs(visited, v)

    def bfs(self, visited, src):
        q = Queue()
        q.put(src)
        while not q.empty():
            curr = q.get()
            if not visited[curr]:
                print(curr)
                visited[curr] = True
                for v in self.adj[curr]:
                    q.put(v)


class GraphAdjMatrix:
    def __init__(self, V):
        self.V = V
        self.matrix = [[0 for _ in range(self.V + 1)] for _ in range(self.V + 1)]

    def build_graph(self, edges):
        for u, v in edges:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1

    def dfs(self, visited, src):
        print(src)
        visited[src] = True
        for v in range(self.V + 1):
            if self.matrix[src][v] == 1 and not visited[v]:
                self.dfs(visited, v)


if __name__ == "__main__":
    g = GraphAdjList(5)
    graph = [[1, 2], [1, 5], [2, 5], [2, 3], [2, 4], [3, 4], [4, 5]]
    g.build_graph(graph)
    visited = [False for _ in range(g.V + 1)]
    g.dfs(visited, 1)
    visited = [False for _ in range(g.V + 1)]
    g.bfs(visited, 1)
    visited = [False for _ in range(g.V + 1)]
    gm = GraphAdjMatrix(5)
    gm.build_graph(graph)
    gm.dfs(visited, 1)


# Backtracking
# Combination Sum I & II
class Solution:
    def combinationSum(self, candidates, target: int):
        res = []

        def helper(start, tsum, track):
            if tsum > target:
                return
            if sum(track) == target:
                res.append(track[:])
                return

            for i in range(start, len(candidates)):
                track.append(candidates[i])
                helper(i, tsum + candidates[i], track)
                track.pop()

        helper(0, 0, [])
        return res

    def combinationSum2(self, candidates, target: int):
        res = []
        candidates.sort()

        def helper(start, tsum, track):
            if tsum > target:
                return
            if sum(track) == target:
                res.append(track[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                track.append(candidates[i])
                helper(i + 1, tsum + candidates[i], track)
                track.pop()

        helper(0, 0, [])
        return res
