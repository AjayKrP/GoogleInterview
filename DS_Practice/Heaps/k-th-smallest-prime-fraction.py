from queue import PriorityQueue


class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        pq = PriorityQueue()
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if arr[j] != 0:
                    pq.put((arr[i]/arr[j], [arr[i], arr[j]]))

        result = None
        while k:
            result = pq.get()[1]
            k -=1

        return result

