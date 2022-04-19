class Solution1:
    def findMaximumXOR(self, nums) -> int:
        n = len(nums)
        ans = float('-inf')
        for i in range(n):
            for j in range(i, n):
                ans = max(ans, nums[i] ^ nums[j])
        return ans


class Solution:
    def findMaximumXOR(self, nums) -> int:
        class Trie:
            def __init__(self, char):
                self.char = char
                self.childs = [None, None]

        trie = Trie('*')

        for num in nums:
            curr = trie
            for j in range(31, -1, -1):
                kth_bit = (num >> j) & 1
                if curr.childs[kth_bit] is None:
                    curr.childs[kth_bit] = Trie(kth_bit)
                curr = curr.childs[kth_bit]

        ans = 0

        for num in nums:
            curr = trie
            curr_ans = 0
            for j in range(31, -1, -1):
                kth_bit = (num >> j) & 1
                if curr.childs[kth_bit ^ 1] is not None:
                    curr_ans += (1 << j)
                    curr = curr.childs[kth_bit ^ 1]
                else:
                    curr = curr.childs[kth_bit]
            ans = max(ans, curr_ans)

        return ans

# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/1669141/Python-oror-Trie
