class Solution:
    def palindromePairs(self, words):
        n = len(words)
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                word = words[i] + words[j]
                if word == word[::-1]:
                    res.append([i, j])
                word = words[j] + words[i]
                if word == word[::-1]:
                    res.append([j, i])
        return res
