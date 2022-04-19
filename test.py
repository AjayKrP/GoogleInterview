# from collections import Counter
#
#
# def findAllPossibleString(words, track, res):
#     if len(track) == len(words):
#         print(track)
#         res.append(track)
#         return res
#
#     for word in words:
#         if word in track:
#             continue
#         track.append(word)
#         findAllPossibleString(words, track, res)
#         track.pop()
#     return res
#
# # res = []
# # print(findAllPossibleString('abc', [], res))
# # print(res)
#
#
# class Solution:
#     def maxLength(self, arr) -> int:
#         return self.dfs(arr, 0, "")
#
#     def dfs(self, arr, pos: int, res: str) -> int:
#         if len(res) != len(set(res)):
#             return 0
#         best = len(res)
#         for i in range(pos, len(arr)):
#             best = max(best, self.dfs(arr, i + 1, res + arr[i]))
#         return best
#
# sol = Solution()
# print(sol.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
#
#
# from queue import Queue
#
# def reverseQueue(queue):
#     stack = []
#     while not queue.empty(): # Add all queue items to stack
#         stack.append(queue.get())
#     while len(stack): # Now put all stack items to queue
#         queue.put(stack.pop())
#     return queue
#
# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q.queue)
# q = reverseQueue(q)
# print(q.queue)
#
#
#

# n = 4
# cost = [[(i, j) for i in range(n + 1)] for j in range(n + 1)]
#
# for L in range(1, n + 1):
#     for i in range(n - L + 2):
#         j = i + L - 1
#         for k in range(i, j + 1):
#             print(cost[i][k])


# name = "alex"
# typed = "aaleex"
#
#
# # saeed
# # ssaaedd
#
# def check(name, typed):
#     ord1 = {}
#     ord2 = {}
#     left = 0
#     right = 0
#
#     while len(name) > right >= left:
#         cnt = 0
#         print(left, right)
#         while right < len(name) and name[left] == name[right]:
#             cnt += 1
#             ord1[(left, name[left])] = cnt
#             right += 1
#
#         left += 1
#
#     left = 0
#     right = 0
#
#     while len(typed) > right >= left:
#         cnt = 0
#         print(left, right)
#         while len(typed) > right >= left and typed[left] == typed[right]:
#             cnt += 1
#             ord2[(left, typed[left])] = cnt
#             right += 1
#
#         left += 1
#     print(ord1)
#     print(ord2)
#     var = iter(ord1)
#     for item in ord2.items():
#         _ = next(var)
#         print(_)
#         if item[0] == _[0] and _[1] <= item[1]:
#             continue
#         else:
#             return False
#     return True
#
#
# print(check('alex', 'aaleex'))
# print(check('saeed', 'ssaaedd'))

# arr = [2, 3, 4, -1, 7]
# target = 5
# dist = float('inf')
# ele = None
# for i in range(len(arr)):
#     curr = abs(target - arr[i])
#     if curr < dist:
#         ele = arr[i]
#         dist = min(dist, curr)
#
# print(dist, ele)


# def is_subsequence(a, b):
#     i = 0
#     j = 0
#     while j < len(b):
#         if i == len(a):
#             return True
#         if a[i] == b[j]:
#             i += 1
#         j += 1
#     return i == len(a)


# def max_subsequence(a, b, i, j):
#     if i >= len(a) or j >= len(b):
#         return 0
#     if a[i] == b[j]:
#         return 1 + max_subsequence(a, b, i + 1, j + 1)
#     return max_subsequence(a, b, i+1, j+1)
#

# print(is_subsequence('abchhhhh', 'aaabcbjskdfsdc'))

def merge(l, mid, h):
    print(l, mid, h)


def merge_sort(l, h):
    if l < h:
        mid = (l + h) // 2
        merge_sort(l, mid)
        merge_sort(mid + 1, h)
        merge(l, mid, h)


merge_sort(1, 8)


def get_movies(movies, duration):
    movies.sort()
    l, r = 0, len(movies) - 1
    currMax = float('-inf')
    p = [-1, -1]
    while l <= r:
        tmp = movies[l] + movies[r]
        if currMax <= tmp <= duration:
            if tmp != currMax:
                currMax = tmp
                p[0] = l
                p[1] = r
            else:
                if max(p[0], p[1]) < max(movies[l], movies[r]):
                    currMax = tmp
                    p[0] = l
                    p[1] = r
            l += 1
        else:
            r -= 1
    print(p)


get_movies([27, 1, 10, 39, 12, 52, 32, 67, 76], 77)

class Solution:
    def dataRepresentation(self, itemAssociation):

        uniqueItems = set()
        items = dict()

        for association in itemAssociation:
            # print(association)
            uniqueItems.add(association[0])
            if association[0] not in items:
                items[association[0]] = [association[1]]
            else:
                items[association[0]].append(association[1])

            if association[1] not in items:
                items[association[1]] = [association[0]]
            else:
                items[association[1]].append(association[0])

        return items, uniqueItems

    def largestItemAssociation(self, itemAssociation):

        results = []

        items, nodes = self.dataRepresentation(itemAssociation)
        visited = set()

        for node in nodes:
            if node in visited:
                continue
            else:
                result = []
                self.startDFS(node, items, visited, result)
                if len(results) == 0:
                    results.append(sorted(result))
                elif len(result) > len(results[0]):
                    [
                        # remove](https://leetcode.com/problems/remove-nth-node-from-end-of-list) previous results and just overwrite
                        results = sorted(result)
                elif len(result) == len(results[0]):  # Got a candidate
                    results.append(sorted(result))
        return sorted(results)

    def startDFS(self, node, items, visited, result):

        visited.add(node)

        for neigbour in items[node]:
            if neigbour in visited:
                continue
            self.startDFS(neigbour, items, visited, result)
        result.append(node)
