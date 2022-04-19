import sys
from queue import PriorityQueue

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
V = 9


def get_min_index(dist, visited):
    min_ = sys.maxsize
    min_index = 0

    for u in range(V):
        if dist[u] < min_ and not visited[u]:
            min_index = u
            min_ = dist[u]
    return min_index


def get_min_index(dist, visited):
    min_ = sys.maxsize
    min_index = 0

    for u in range(V):
        if dist[u] < min_ and not visited[u]:
            min_index = u
            min_ = dist[u]
    return min_index


def djkastra_pq(src):
    dist = [sys.maxsize for _ in range(V)]
    dist[src] = 0
    visited = [False for _ in range(V)]
    pq = PriorityQueue()
    pq.put(src)
    while not pq.empty():
        u = pq.get()
        visited[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                pq.put(v)

    print(dist)


def djkastra(src):
    dist = [sys.maxsize for _ in range(V)]
    dist[src] = 0
    visited = [False for _ in range(V)]

    for _ in range(V):
        u = get_min_index(dist, visited)
        visited[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print(dist)


def bellman_ford(src):
    dist = [sys.maxsize for _ in range(V)]
    dist[src] = 0
    for u in range(V - 1):
        for v in range(V):
            if graph[u][v] > 0 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print(dist)


djkastra_pq(0)
djkastra(0)
bellman_ford(0)
