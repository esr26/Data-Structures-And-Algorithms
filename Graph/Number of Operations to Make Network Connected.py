class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        size = [1] * n
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False

            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u

            parent[root_v] = root_u
            size[root_u] += size[root_v]
            return True

        for u, v in connections:
            if union(u, v):
                components -= 1

        return components - 1
