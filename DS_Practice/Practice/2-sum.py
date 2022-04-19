class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
        result=[]
        dic={}
        for i in range(len(A)):
            if A[i] in dic:
               result.append([dic[A[i]],i+1])
            else:
                if B-A[i] not in dic:
                    dic[B-A[i]]=i+1
                
        return result[0] if len(result)>0 else []
