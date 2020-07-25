from collections import defaultdict
import heapq

grid = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]


# Complete the shortestReach function below.
from collections import defaultdict
import heapq
def shortestReach(n, edges, s):
    # build the graph
    graph = defaultdict(list)
    for start, end, distance in edges:
        graph[start].append((distance, end))
        graph[end].append((distance, start))

    print(edges)
    visited = [None for i in range(n + 1)]
    distance = [float('inf') for i in range(n + 1)]

    #start node
    distance[s] = 0
    heap = [(distance[s], s)]
    # heapq.heapify(heap)

    while heap:
        dist, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        for w, length in graph[v]:
            if not visited[length] and distance[length] > dist + w:
                distance[length] = dist + w
                heapq.heappush(heap, (distance[length], length))
    del distance[s]
    del distance[0]
    print([-1 if d == float('inf') else d for d in distance])
    return [-1 if d == float('inf') else d for d in distance]


shortestReach(4, grid, 1)