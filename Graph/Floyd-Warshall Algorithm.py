class Solution:
    def floydWarshall(self, n, edges):
        inf = float("inf")

        dist = [[inf] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, weight in edges:
            dist[u][v] = min(dist[u][v], weight)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j],
                        )

        has_negative_cycle = any(dist[i][i] < 0 for i in range(n))

        return dist, has_negative_cycle
