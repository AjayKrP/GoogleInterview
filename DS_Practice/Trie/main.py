class Trie:
    def __init__(self, char=None):
        self.char = char
        self.we = 0
        self.childs = [None] * 26


class TrieDS:
    @staticmethod
    def insert(root, word):
        if not isinstance(word, str):
            raise ValueError('Input value is not correct!')

        lastNode = root
        for char in word:
            idx = ord(char) - ord('a')
            if lastNode.childs[idx] is None:
                lastNode.childs[idx] = Trie(char)
            lastNode = lastNode.childs[idx]
        lastNode.we = 1

    @staticmethod
    def search(root, word):
        lastNode = root
        for char in word:
            idx = ord(char) - ord('a')
            if lastNode.childs[idx] is None:
                return False
            lastNode = lastNode.childs[idx]
        return lastNode.we == 1


root = Trie()
trie = TrieDS()


def test_trie_insert():
    trie.insert(root, 'apple')
    trie.insert(root, 'mango')
    # trie.insert(root, 32234)
    # trie.insert(root, '1234a')


def test_trie_search():
    assert trie.search(root, 'apple')
    assert trie.search(root, 'dog')


def test_trie():
    test_trie_insert()
    test_trie_search()
