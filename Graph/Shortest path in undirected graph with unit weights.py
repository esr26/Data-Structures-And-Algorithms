from collections import deque

class Solution:
    def shortestPath(self, edges, N, M):
        graph = [[] for _ in range(N)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist = [-1] * N
        dist[0] = 0

        queue = deque([0])

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    queue.append(nei)

        return dist

        