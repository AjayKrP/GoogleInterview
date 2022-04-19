from typing import List


# max product subarray
class Solution1:
    def maxProduct(self, nums) -> int:
        maxEnding = nums[0]
        minEnding = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxEnding, minEnding = minEnding, maxEnding
            maxEnding = max(nums[i], maxEnding * nums[i])
            minEnding = min(nums[i], minEnding * nums[i])
            res = max(res, max(maxEnding, minEnding))
        return res


# Surrounded Regions
from queue import Queue


class Solution2:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def boundary(front, m, n):
            return front[0] == 0 or front[0] == m - 1 or front[1] == 0 or front[1] == n - 1

        m, n = len(board), len(board[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit and not boundary((i, j), m, n) and board[i][j] == 'O':
                    q = Queue()
                    q.put((i, j))
                    visit.add((i, j))
                    surrounded = True
                    while not q.empty():
                        front = q.get()
                        if boundary(front, m, n):
                            surrounded = False
                            break
                        for d in directions:
                            cx = d[0] + front[0]
                            cy = d[1] + front[1]
                            if cx < 0 or cx >= m or cy < 0 or cy >= n:
                                continue
                            if (cx, cy) not in visit and board[cx][cy] == 'O':
                                q.put((cx, cy))
                                visit.add((cx, cy))
                    if surrounded:
                        for item in visit:
                            board[item[0]][item[1]] = 'X'


# Decode ways
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == '2' and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res

            return res

        return dfs(0)


# Node with k distance
from collections import defaultdict
from queue import Queue


class Solution3(object):
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


# https://www.lintcode.com/problem/1160/description
class Solution4:
    """
    @param workers: workers' location
    @param bikes: bikes' location
    @return: assign bikes
    """

    def assignBikes(self, workers, bikes):
        # write your code here

        n = len(workers)
        m = len(bikes)
        sol = [0 for i in range(n * m)]
        for i in range(n):
            for j in range(m):
                cost = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                sol[i * m + j] = [cost, i, j]

        sol.sort()

        visisted_worker = [False] * n
        visisted_bike = [False] * m

        ans = [0 for i in range(n)]
        for i in range(len(sol)):
            cost, workersIdx, bikeIdx = sol[i]
            if visisted_worker[workersIdx] == False and visisted_bike[bikeIdx] == False:
                visisted_worker[workersIdx] = visisted_bike[bikeIdx] = True
                ans[workersIdx] = bikeIdx
        return ans


sol = Solution4()
print(sol.assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]]))
print(sol.assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))


# Movies in flight
def moviesOnFlight(movieDurations, d):
    d = d - 30

    m = []
    for i, m_x in enumerate(movieDurations):
        m.append((m_x, i))

    m.sort(key=lambda x: x[0])

    i = 0
    j = len(m) - 1

    max_sum = 0
    max_sum_pair = None
    while i < j:
        movie_sum = m[i][0] + m[j][0]
        if movie_sum > d:
            j -= 1
        elif movie_sum <= d:
            if movie_sum > max_sum:
                max_sum = movie_sum
                max_sum_pair = (m[i][1], m[j][1])
            elif movie_sum == max_sum:
                if m[i][0] > m[max_sum_pair[0]][0] or m[j][0] > m[max_sum_pair[1]][0]:
                    max_sum_pair = (m[i][1], m[j][1])
            i += 1

    return max_sum_pair


# Association group
import collections


def func(l):
    visited = []
    d = collections.defaultdict(list)

    def dfs(item, output):
        if item not in visited:
            visited.append(item)
            output.append(item)
            for neighbor in d[item]:
                dfs(neighbor, output)

    if len(l) < 2:
        return l

    for item in l:
        if len(item) == 1:
            d[item[0]] = []
        else:
            d[item[0]].append(item[1])
            d[item[1]].append(item[0])

    res = []
    for item in d:
        if item not in visited:
            output = []
            dfs(item, output)
            output.sort()
            if len(res) == 0 or len(output) > len(res):
                res = output
            elif len(output) == len(res):
                res = min(res, output)

    return res


from queue import Queue


# max area of rectangle
class Solution6:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        visited = [[False for _ in range(n)] for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                localMax = 0
                if grid[i][j] == 1 and not visited[i][j]:
                    q = Queue()
                    q.put((i, j))
                    visited[i][j] = True
                    while not q.empty():
                        tmp = q.get()
                        i_ = tmp[0]
                        j_ = tmp[1]
                        localMax += 1
                        for k in range(4):
                            nr = i_ + dr[k]
                            nc = j_ + dc[k]
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and not visited[nr][nc]:
                                q.put((nr, nc))
                                visited[nr][nc] = True
                    max_area = max(localMax, max_area)

        return max_area


# maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
class Solution7:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.sort()
        verticalCuts.sort()

        verticalCuts = [0] + verticalCuts + [w]

        horizontalCuts = [0] + horizontalCuts + [h]

        max_width = 0
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        max_height = 0
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        return (max_height * max_width) % ((10 ** 9) + 7)


# Gas station
class Solution8:
    def canCompleteCircuit(self, gas, cost) -> int:
        balance = 0
        ans = 0
        total_sum = 0
        sum_ = 0
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            sum_ += gas[i] - cost[i]
            if sum_ < 0:
                sum_ = 0
                ans = i + 1
                i = ans
        return ans if total_sum >= 0 else -1


from queue import Queue
from collections import defaultdict


# Number of provinces/Friends group
class Solution9:
    def findCircleNum(self, isConnected) -> int:
        visited = [0] * len(isConnected[0])
        amount_of_provinces = len(isConnected[0])
        count = 0

        def dfs_util(province):
            visited[province] = 1

            for j in range(amount_of_provinces):
                if isConnected[province][j] == 1 and visited[j] == 0:
                    dfs_util(j)

        for i in range(0, len(visited)):
            if visited[i] == 0:
                count += 1
                dfs_util(i)

        return count


# Sentence Similarity
class Solution10:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """

    def is_sentence_similarity(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # write your code here

        if len(words1) != len(words2):
            return False
        word_mapping = {}
        for pair in pairs:
            word_mapping[pair[0]] = pair[1]
            word_mapping[pair[1]] = pair[0]

        for i in range(len(words2)):
            if words1[i] == words2[i]:
                continue
            if words1[i] in word_mapping and word_mapping[words1[i]] == words2[i] or words2[i] in word_mapping and \
                    word_mapping[words2[i]] == words1[i]:
                continue
            else:
                return False
        return True


# https://medium.com/@rebeccahezhang/leetcode-737-sentence-similarity-ii-2ca213f10115


# Min cost to join ropes of given lengths

from queue import PriorityQueue


def connect_ropes(ropes):
    pq = PriorityQueue()
    for rope in ropes:
        pq.put(rope)
    res = 0
    while not pq.empty() and pq.qsize() > 1:
        item1 = pq.get()
        item2 = pq.get()
        res += max(res, item1 + item2)
        pq.put(item1 + item2)
    return res


print(connect_ropes([4, 3, 2, 6]))

# Populating next right pointer
from queue import Queue


class Solution12:
    def connect(self, root):
        if root is None:
            return root
        q = Queue()
        q.put(root)
        while not q.empty():
            qL = q.qsize()
            track = []
            while qL:
                front = q.get()
                if front.left:
                    q.put(front.left)
                    track.append(front.left)
                if front.right:
                    q.put(front.right)
                    track.append(front.right)
                qL -= 1
            for i in range(1, len(track)):
                track[i - 1].next = track[i]
            track.clear()
        return root


# Knight Moves Problem
def knight_moves(start_position, k):
    moves = [[1, 2], [2, 1], [1, -2], [-1, 2], [-1, -2], [-2, -1], [2, -1], [-2, 1]]
    q = Queue()
    checked = [[False for _ in range(8)] for _ in range(8)]

    q.put(start_position)
    count = 0

    while k:
        qL = q.qsize()
        while qL:
            position = q.get()
            for move in moves:
                cx = move[0] + position[0]
                cy = move[1] + position[1]
                if cx < 0 or cy > 7 or cy < 0 or cy > 7 or checked[cx][cy]:
                    continue
                checked[cx][cy] = True
                q.put((cx, cy))
                count += 1
            qL -= 1
        k -= 1
    return count


# Fresh promotion
def fresh_promotion(code_list, shopping_cart):
    cart_idx = 0
    code_list_idx = 0
    while code_list_idx < len(code_list) and cart_idx < len(shopping_cart):
        code = code_list[code_list_idx]
        code_idx = 0
        while code_idx < len(code) and cart_idx < len(shopping_cart):
            if code[code_idx] == shopping_cart[cart_idx] or code[code_idx] == 'anything':
                code_idx += 1
            else:
                code_idx = 0
            cart_idx += 1
        if code_idx == len(code):
            code_list_idx += 1
    if code_list_idx == len(code_list):
        return 1
    return 0


print(fresh_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                      ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))

print(fresh_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                      ['banana', 'orange', 'banana', 'apple', 'apple']))

print(fresh_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                      ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']))

print(fresh_promotion([['apple', 'apple', 'apple', 'banana', 'apple']], ['apple', 'apple', 'apple', 'banana']))


# Top-N Competitor Problem
def topcompetitors(numComp, topComp, comps, numReviews, reviews):
    comps.sort()
    d = {}
    output = []
    for i in comps:
        d[i] = 0

    for review in reviews:
        review = review.split()
        for word in review:
            if word in d:
                d[word] += 1
                break

    for _ in range(topComp):
        maxval = 0
        maxkey = ''
        for key, val in d.items():
            if val > maxval:
                maxval = val
                maxkey = key
        output.append(maxkey)
        del d[maxkey]
    return output


numComp = 6
topComp = 2
comps = ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular']
numReviews = 6
reviews = [
    "newshop is providing good services in the city; everyone should use newshop",
    "best services by newshop",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "newshop has awesome services",
    "Thanks newshop for the quick delivery"]

print(topcompetitors(numComp, topComp, comps, numReviews, reviews))

# Treasure Island Problem
from collections import deque


def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    matrix = [row[:] for row in m]
    nrow, ncol = len(matrix), len(matrix[0])

    q = deque([((0, 0), 0)])  # ((x, y), step)
    matrix[0][0] = "D"
    while q:
        (x, y), step = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x + dx < nrow and 0 <= y + dy < ncol:
                if matrix[x + dx][y + dy] == "X":
                    return step + 1
                elif matrix[x + dx][y + dy] == "O":
                    # mark visited
                    matrix[x + dx][y + dy] = "D"
                    q.append(((x + dx, y + dy), step + 1))

    return -1


# Transaction Logs
def transaction_logs(arr, threshold):
    res = []
    dict = collections.defaultdict(int)
    for each_rows in arr:
        row = ''.join(each_rows)
        temp = row.split()
        if temp[0] != temp[1]:
            dict[temp[1]] += 1
        dict[temp[0]] += 1

    for key, val in dict.items():
        if val >= threshold:
            res.append(key)
    return res


# Optimal Utilization
class Solution14:
    def findPairs(self, a, b, target):
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1])
        l, r = 0, len(b) - 1
        ans = []
        curDiff = float('inf')
        while l < len(a) and r >= 0:
            id1, i = a[l]
            id2, j = b[r]
            if target - i - j == curDiff:
                ans.append([id1, id2])
            elif i + j <= target and target - i - j < curDiff:
                ans.clear()
                ans.append([id1, id2])
                curDiff = target - i - j
            if target > i + j:
                l += 1
            else:
                r -= 1
        return ans


# Favorite Genres
def favorite_genres(userSongs, songGenres):
    songs_to_genres_mapping = {}
    for genres in songGenres.keys():
        for song in songGenres[genres]:
            songs_to_genres_mapping[song] = genres

    for user in userSongs.keys():
        favorite_songs = {}
        songs = userSongs[user]
        max_cnt = 0
        for song in songs:
            genre = songs_to_genres_mapping[song] if song in songs_to_genres_mapping else None
            if genre in favorite_songs:
                favorite_songs[genre] += 1
            else:
                favorite_songs[genre] = 1
            max_cnt = max(max_cnt, favorite_songs[genre])
        output = {k: v for k, v in sorted(favorite_songs.items(), key=lambda x: x[1], reverse=True) if v == max_cnt and k is not None}
        print(output)

userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}
songGenres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"]
}
favorite_genres(userSongs, songGenres)
userSongs = {
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
}
songGenres = {}
favorite_genres(userSongs, songGenres)


# 907. Sum of Subarray Minimums
class Solution15:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        small_before = [-1]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:small_before[i] = stack[-1]
            stack.append(i)
        best = [0]*(n+1)
        ans = 0
        for i in range(n):
            best[i] = best[small_before[i]] + (i - small_before[i])*arr[i]
            ans += best[i]
        return ans%1000000007