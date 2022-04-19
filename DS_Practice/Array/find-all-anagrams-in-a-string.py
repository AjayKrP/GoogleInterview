from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        needs = Counter(p)
        result = []
        left = right = 0
        s = list(s)
        window = {}
        for char in p:
            window[char] = 0

        match = 0
        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left == len(p):
                    result.append(left)
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return result


# sol = Solution()
# print(sol.findAnagrams("cbaebabacd", "abc"))
