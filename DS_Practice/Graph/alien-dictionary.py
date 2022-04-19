# https://medium.com/@timothyhuang514/graph-alien-dictionary-d2b104c36d8e

def sorted_order(words):
    adj = {c: set() for word in words for c in word}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        for i in range(minLen):
            if w1[i] != w2[i]:
                adj[w1[i]].add(w2[i])
                break

    visited = {}
    ans = []

    def dfs(c):
        if c in visited:
            return visited[c]
        visited[c] = True
        for x in adj[c]:
            if dfs(x):
                return True

        visited[c] = False
        ans.append(c)

    dfs('c')
    ans.reverse()
    return ''.join(ans)


# def test_alien_dictionary():
print(sorted_order(['caa', 'aaa', 'aab']))
