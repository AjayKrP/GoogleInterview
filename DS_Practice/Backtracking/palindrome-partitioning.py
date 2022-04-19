class Solution:
    def partition(self, s: str):
        res = []

        def backtrack(i, curr):
            if i >= len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                string = s[i:j + 1]
                if string == string[::-1]:
                    curr.append(s[i:j + 1])
                    backtrack(j + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return res
