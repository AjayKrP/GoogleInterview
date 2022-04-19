from queue import Queue
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])
        
        result = []
        for i in range(n):
            visited = [False for _ in range(n)]
            q = Queue()
            q.put(i)
            level = {}
            level[i] = 0
            dist = 0
            while not q.empty():
                front = q.get()
               
                for item in adj[front]:
                    if not visited[item]:
                        q.put(item)
                        visited[front] = True
                        level[item] = level[front] + 1
                        dist += level[item]
            print(level)
            result.append(dist)
        return result
                    
                
