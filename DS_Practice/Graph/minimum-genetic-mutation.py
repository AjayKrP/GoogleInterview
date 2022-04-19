from collections import defaultdict
from queue import Queue


class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        nei = defaultdict(list)

        if end not in bank:
            return 0

        for word in bank:
            for j in range(len(word)):
                pat = word[:j] + '*' + word[j + 1:]
                nei[pat].append(word)
        visited = {start}
        q = Queue()
        q.put(start)
        res = 1
        while not q.empty():
            ql = q.qsize()
            while ql:
                word = q.get()
                if word == end:
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
