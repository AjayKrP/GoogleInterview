class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k
        while left < right:
            m = (left + right)//2
            if x - arr[m] > arr[m+k] - x:
                left = m + 1
            else:
                right = m
        result = []
        for i in range(left, left + k):
            result.append(arr[i])
        
        return result
        
       
