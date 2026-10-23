class Solution:
    def bellmanFord(self, n, edges, src):
        # Initialize distances.
        dist = [float("inf")] * n
        dist[src] = 0

        # Relax all edges at most n - 1 times.
        for _ in range(n - 1):
            updated = False

            for u, v, weight in edges:
                if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    updated = True

            if not updated:
                break

        # Detect a reachable negative cycle.
        for u, v, weight in edges:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                return -1

        return dist
