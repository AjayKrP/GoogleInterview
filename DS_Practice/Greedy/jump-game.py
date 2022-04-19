class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = []
        n = len(nums)
        for i in range(n):
            successor =  i + nums[i]  
            res.append([i, successor if successor < n else n - 1])
        x = res[0]
        for i in range(1, len(res)):
            curr = res[i]
            if curr[0] <= x[1]:
                x[1] = max(x[1], curr[1])
            else:
                return False
        return True
