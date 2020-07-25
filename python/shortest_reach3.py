import sys

grid = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]

def dijkstra(G, s, n):

    dist = [sys.maxsize] * (n + 1)
    visited = [False] * (n + 1)
    dist[s] = 0

    while True:
        u = -1
        sd = sys.maxsize
        for v in range(1, n + 1):
            if dist[v] < sd and visited[v] == False:
                u = v
                sd = dist[v]
        if u == -1: return dist
        visited[u] = True
        for v in G[u]:
            w = G[u][v]
            newLen = dist[u] + w
            if newLen < dist[v]:
                dist[v] = newLen

    print(dist)

    return dist


dijkstra(4, grid, 1)