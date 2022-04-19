class Trie:
    def __init__(self, char=None):
        self.char = char
        self.we = 0
        self.mc = 0
        self.childs = [None] * 26


class TrieDS:
    @staticmethod
    def insert(root, word):
        mc_max = float('-inf')
        if not isinstance(word, str):
            raise ValueError('Input value is not correct!')
        lastNode = root
        for char in word:
            idx = ord(char) - ord('a')
            if lastNode.childs[idx] is None:
                lastNode.childs[idx] = Trie(char)
            lastNode = lastNode.childs[idx]
            lastNode.mc += 1
            mc_max = max(lastNode.mc, mc_max)
        lastNode.we = 1
        return mc_max


class Solution:
    @staticmethod
    def longestCommonPrefix(strs) -> str:
        root = Trie()
        trie = TrieDS()
        mc_max = float('-inf')
        for word in strs:
            mc_max = max(trie.insert(root, word), mc_max)
        lastNode = root
        out = ''
        for char in strs[0]:
            idx = ord(char) - ord('a')
            if lastNode.childs[idx] is None:
                return out
            lastNode = lastNode.childs[idx]
            if lastNode.mc == len(strs):
                out += lastNode.char
            else:
                break
        return out


sol = Solution()


def test_solution():
    assert sol.longestCommonPrefix(["a"]) == 'a'
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ''
