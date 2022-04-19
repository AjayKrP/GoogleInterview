from queue import Queue


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        mySet = set()
        isPresent = False
        for word in wordList:
            if word == endWord:
                isPresent = True
            mySet.add(word)

        if not isPresent:
            return []

        q = Queue()
        q.put((beginWord, [beginWord]))
        depth = 0
        result = []
        seen = set()
        found = True
        while not q.empty():
            depth += 1
            size = q.qsize()
            while size:
                curr, path = q.get()
                for i in range(len(curr)):
                    tmp = list(curr)
                    for c in range(26):
                        tmp[i] = chr(97+c)
                        fword = ''.join(tmp)
                        if fword == curr:
                            continue
                        if fword == endWord:
                            result.append(path)
                            found = True
                        if fword in mySet:
                            if fword not in seen:
                                q.put((fword, path + [fword]))
                                mySet.remove(fword)
                                seen.add(curr)
                size -= 1
            if found:
                break
        return result
