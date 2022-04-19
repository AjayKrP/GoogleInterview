class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxLen = float('-inf')
        visited = [False]*(len(nums))
        for i in range(len(nums)):
            
            index = i
            cnt = 0
            while not visited[index]:
                visited[index] = True
                index = nums[index]
                cnt += 1
                
            maxLen = max(maxLen, cnt)
        
        return maxLen
        
