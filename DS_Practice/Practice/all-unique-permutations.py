from itertools import permutations
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
        res = permutations(A)
        ans = set()
        for item in res:
            ans.add(item)
        return list(ans)

