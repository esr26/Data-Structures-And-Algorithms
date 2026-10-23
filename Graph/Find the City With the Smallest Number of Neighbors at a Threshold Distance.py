class Solution:
    def findTheCity(
        self,
        n: int,
        edges: list[list[int]],
        distanceThreshold: int,
    ) -> int:
        inf = float("inf")
        dist = [[inf] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, weight in edges:
            dist[u][v] = min(dist[u][v], weight)
            dist[v][u] = min(dist[v][u], weight)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_count = float("inf")
        city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                city = i

        return city
