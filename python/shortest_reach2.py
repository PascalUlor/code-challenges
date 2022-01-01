
from collections import defaultdict
from heapq import heappop, heappush

grid = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]

def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for (u, v), w in edges.items():
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = [False for _ in range(n + 1)]
    distance = [float("inf") for _ in range(n + 1)]
    distance[s] = 0
    minHeap = [(distance[s], s)]
    
    while minHeap:
        d, u = heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        for w, v in graph[u]:
            if not visited[v] and distance[v] > d + w:
                distance[v] = d + w
                heappush(minHeap, (distance[v], v))
    del distance[s]
    del distance[0]
    print([-1 if d == float('inf') else d for d in distance])
    return [-1 if d == float("inf") else d for d in distance]

shortestReach(4, grid, 1)
