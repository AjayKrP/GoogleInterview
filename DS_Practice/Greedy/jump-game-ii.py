class Solution:
    def jump(self, nums: List[int]) -> int:
        res = []
        n = len(nums)
        end = jumps = i = max_node = 0
        
        while end < n-1:
            max_node = max(max_node, i + nums[i])
            
            if i == end:
                end = max_node
                jumps += 1
            i += 1
        
        return jumps

        
