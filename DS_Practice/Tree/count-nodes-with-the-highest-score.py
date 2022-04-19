from collections import defaultdict


class Solution:
    def countHighestScoreNodes(self, parents):
        adj = defaultdict(list)
        nodes = [x for x in range(len(parents))]

        # create graph
        for i in range(len(nodes)):
            if parents[i] == -1:
                parents[i] = 0
            if not parents[i] == i:
                adj[i].append(parents[i])
                adj[parents[i]].append(i)

        print(adj)

        degree = []

        for i in range(len(parents)):
            cnt = 1
            for item in adj[i]:
                cnt *= (len(adj[i]) - adj[item].count(i) + 1)
            degree.append(cnt)

        print(degree)