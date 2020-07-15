import collections
class Solution:
    def networkDelayTime(self, times, N, K):
        g = collections.defaultdict(list)
        for u, v, w in times:
            g[u - 1].append((w, v - 1))

        pq = [[float("inf"), x] for x in range(N)]
        d = [float("inf") for v in range(N)]  # final distance from source
        d[K - 1] = 0  # make source dist 0
        pq[K - 1][0] = 0
        pq = MinHeap(pq)
        
        while pq.size > 0:
            w, u = pq.pop()
            for d2, v in g[u]:
                if pq.is_present(v):
                    if d[v] > w + d2 and d[u] != float("inf"):
                        d[v] = w + d2
                        pq.update(v, w + d2)
        m = max(d)
        return m if m != float("inf") else -1


class MinHeap:
    def __init__(self, a):
        self.h = a
        self.p = [x for x in range(len(a))]  # Store positions of nodes to search quickly if neighbor is present in heap
        self.size = len(a)
        for x in range((len(a) - 1) // 2, -1, -1):
            self.heapify(x)

    def heapify(self, i):
        h, p = self.h, self.p
        mi = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.size and h[l][0] < h[mi][0]:
            mi = l
        if r < self.size and h[r][0] < h[mi][0]:
            mi = r
        if mi != i:
            p[h[mi][1]], p[h[i][1]] = i, mi
            h[mi], h[i] = h[i], h[mi]
            self.heapify(mi)

    def update(self, i, val):
        h, p = self.h, self.p
        i = p[i]
        h[i][0] = val
        while i > 0:
            parent = (i - 1) // 2
            if h[i][0] < h[parent][0]:
                p[h[parent][1]], p[h[i][1]] = i, parent
                h[parent], h[i] = h[i], h[parent]
                i = parent
            else:
                break

    def is_present(self, i):
        if self.p[i] < self.size:
            return True
        return False

    def pop(self):
        h, p, = self.h, self.p,
        root = h[0]

        # Replace root node with last node
        last = h[self.size - 1]
        h[0] = last

        # Update position of last node
        p[last[1]] = 0
        p[root[1]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.heapify(0)

        return root