import bisect
from functools import lru_cache
from queue import Queue
from typing import List

N = 4
grid = [[1 for _ in range(N + 1)] for _ in range(N + 1)]
moves = [[1, 2], [2, 1], [1, -2], [-2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1]]
d = (3, 3)
s = (1, 1)


def knight_moves(x, y, res, d):
    if x < 0 or x > N or y < 0 or y > N:
        return 0

    if (x, y) == d:
        return res
    if grid[x][y] == 0:
        return res
    curr = grid[x][y]
    grid[x][y] = 0
    for d in moves:
        return min(res, knight_moves(x + d[0], y + d[1], res, d)) + 1

    grid[x][y] = curr

    return res


result = knight_moves(1, 1, float('inf'), d)
print(-1 if result == float('inf') else result)


# Maximum Earnings From Taxi
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[0])
        profit = [rides[i][1] - rides[i][0] + rides[i][2] for i in range(len(rides))]
        starts = [rides[i][0] for i in range(len(rides))]

        @lru_cache(None)
        def dp(i):
            if i == len(rides):
                return 0

            res = dp(i + 1)  # not choose the ith ride
            nextStart = bisect.bisect_left(starts, rides[i][1])
            res = max(res, profit[i] + dp(nextStart))  # possibly choose the ith ride
            return res

        return dp(0)


def pantry(a, b, x, y):
    """
    If a+b is odd/even x+y also needs to be odd/even else return -1;
    if a==x && b==y return 0;
    if a+b==c+d || a-b==c-d return 1;
    else return 2;
        :return:
    """
    if (x + y) % 2 != (a + b) % 2:
        return -1
    if a == x and b == y:
        return 0
    if a + b == x + y or a - b == x - y:
        return 1
    return 2


print(pantry(1, 1, 3, 3))

"""
int findMinArrowShots(int[][] intvs) {
    // ...

    for (int[] interval : intvs) {
        int start = interval[0];
        // Change >= into >
        if (start > x_end) {
            count++;
            x_end = interval[1];
        }
    }
    return count;
}
"""


def getMin(invt):
    count = 0
    prev = float('-inf')
    for interval in invt:
        start = interval[0]
        if start > prev:
            count += 1
        prev = start
    return count


def findMinArrowShots(invt):
    if len(invt) == 0:
        return 0
    horizontal = sorted(invt, key=lambda x: x[0])
    vertical = sorted(invt, key=lambda x: x[1])
    h = getMin(horizontal)
    v = getMin(vertical)
    print(h, v)
    return min(h, v)


print(findMinArrowShots([[0, 2],
                         [1, 0],
                         [1, 1],
                         [1, 2]]))
print(findMinArrowShots([[15, 21], [33, 8], [17, 21], [17, 8], [28, 11], [28, 19]]))
print(findMinArrowShots([[15, 1], [15, 2], [15, 3], [15, 4], [18, 1], [20, 1]]))
