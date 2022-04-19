from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        mySet = set()
        isPresent = False
        for word in wordList:
            if word == endWord:
                isPresent = True
            mySet.add(word)

        if not isPresent:
            return 0

        q = Queue()
        q.put(beginWord)
        depth = 0
        while not q.empty():
            depth += 1
            size = q.qsize()
            while size:
                curr = q.get()
                for i in range(len(curr)):
                    tmp = list(curr)
                    for c in range(26):
                        tmp[i] = chr(97+c)
                        fword = ''.join(tmp)
                        if fword == curr:
                            continue
                        if fword == endWord:
                            return depth + 1
                        if fword in mySet:
                            q.put(fword)
                            mySet.remove(fword)

                size -= 1


from collections import defaultdict
from queue import Queue


class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)

        if endWord not in wordList:
            return 0

        for word in wordList:
            for j in range(len(word)):
                pat = word[:j] + '*' + word[j + 1:]
                nei[pat].append(word)
        visited = {beginWord}
        q = Queue()
        q.put(beginWord)
        res = 1
        while not q.empty():
            ql = q.qsize()
            while ql:
                word = q.get()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pat = word[:j] + "*" + word[j + 1:]
                    for n in nei[pat]:
                        if n not in visited:
                            visited.add(n)
                            q.put(n)
                ql -= 1
            res += 1
        return 0


