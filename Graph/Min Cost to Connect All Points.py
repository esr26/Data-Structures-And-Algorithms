class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            root_a = find(u)
            root_b = find(v)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                parent[root_a] = root_b
                size[root_b] += size[root_a]
            else:
                parent[root_b] = root_a
                size[root_a] += size[root_b]

            return True

        n = len(points)
        if n <= 1:
            return 0

        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, weight))

        parent = list(range(n))
        size = [1] * n
        edges.sort(key=lambda edge: edge[2])

        total_weight = 0
        edges_used = 0

        for u, v, weight in edges:
            if union(u, v):
                total_weight += weight
                edges_used += 1

                if edges_used == n - 1:
                    break

        return total_weight if edges_used == n - 1 else -1
