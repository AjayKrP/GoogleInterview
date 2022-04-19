class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preMul = [1 for _ in range(n+1)]
        zeroCount = 0
        mul = 1
        for i in range(n):
            if nums[i] != 0:
                preMul[i+1] = preMul[i]*nums[i]
            else:
                if zeroCount < 1:
                    for j in range(n):
                        if i != j:
                            mul *= nums[j]
                else:
                    mul = 0
                preMul[i+1] = preMul[i]*nums[i]
                zeroCount += 1
                
        ans = []
        
        print(nums)
        print(preMul)
        for i in range(n):
            ans.append(preMul[-1]//nums[i] if nums[i] != 0 else mul)
        
        return ans
        
