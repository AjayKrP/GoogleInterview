class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(self.nums)
        self.preSum = [0 for _ in range(n+1)]
        for i in range(n):
            self.preSum[i+1] = self.preSum[i] + self.nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
