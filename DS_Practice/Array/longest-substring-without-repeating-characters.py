from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = right = 0
        s = list(s)
        window = {}
        for char in s:
            window[char] = 0
        res = 0
        while right < len(s):
            c1 = s[right]
            window[c1] += 1
            right += 1
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1
            res = max(res, right - left)
        return res
