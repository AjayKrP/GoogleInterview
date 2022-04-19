class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = {}
        for c in t:
            if c not in needed:
                needed[c] = 1
            else:
                needed[c] += 1

        window = {}
        nextPosition = 0
        i = left = start = 0
        match = 0
        res = float('inf')
        while i < len(s):
            c1 = s[i]
            if c1 in needed and needed[c1] > 0:
                if c1 in window:
                    window[c1] += 1
                else:
                    window[c1] = 1
                if window[c1] == needed[c1]:
                    match += 1

            i += 1

            while match == len(needed):
                if i - left < res:
                    start = left
                    res = i - left
                c2 = s[left]
                if c2 in needed and needed[c2] > 0:
                    window[c2] -= 1
                    if window[c2] < needed[c2]:
                        match -= 1
                left += 1
        return "" if res == float('inf') else s[start:res]


sol = Solution()
print(sol.minWindow('ADOBECODEBANC', 'ABC'))
