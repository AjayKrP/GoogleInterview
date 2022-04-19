from queue import PriorityQueue

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        pq = PriorityQueue()
        m = len(matrix)
        n = len(matrix[1])

        for i in range(m):
            for j in range(n):
                pq.put(matrix[i][j])
        item = -1
        while k:
            item = pq.get()
            k -= 1
        return item
