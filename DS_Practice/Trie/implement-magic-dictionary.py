class TrieDS:
    def __init__(self):
        self.root = {}

    def insert(self, dictionary):
        for word in dictionary:
            curr = self.root
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['~'] = True

    def search(self, word):
        return self.dfs(self.root, word, 0, 0)

    def dfs(self, root, searchWord, diff, i):
        if i == len(searchWord):
            if root.we == 1 and diff == 1:
                return True
            return False
        res = False
        if diff == 0:
            for letter in root:
                if letter == searchWord[i] or letter == '~':
                    continue
                res = res or self.dfs(root[letter], searchWord, diff + 1, i + 1)
        if searchWord[i] in root:
            res = res or self.dfs(root[searchWord[i]], searchWord, diff, i + 1)
        return res


class MagicDictionary:

    def __init__(self):
        self.trie = TrieDS()

    def buildDict(self, dictionary) -> None:
        self.trie.insert(dictionary)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


# https://leetcode.com/problems/implement-magic-dictionary/discuss/1577539/Python-Simple-Trie-%2B-DFS-Recursive-Solution-with-Explanation
