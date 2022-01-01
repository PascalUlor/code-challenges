def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #Dijkstra algorithm
        """
        cost formula
        if (dist(u) + cost(u,v)) < dist(v):
            dist(v) = dist(u) + cost(u,v)
        """
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)
        for start, end, time in times:
            graph[start - 1].append((end - 1, time))
        
        nodes = [None for i in range(N)]

        heap = [(0, K - 1)]
        heapq.heapify(heap)

        while heap:
            dist, v = heapq.heappop(heap)
            if nodes[v] == None:
                nodes[v] = dist
                for w, length in graph[v]:
                    if nodes[w] == None:
                        heapq.heappush(heap, (dist + length, w))

        if None in nodes:
            return -1
        return max(nodes)