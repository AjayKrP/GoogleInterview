from itertools import permutations
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):

        res = []
        for item in permutations(A):
            res.append(item)
        return res

