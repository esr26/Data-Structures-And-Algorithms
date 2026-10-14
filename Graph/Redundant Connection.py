class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                parent[root_a] = root_b
                size[root_b] += size[root_a]
            else:
                parent[root_b] = root_a
                size[root_a] += size[root_b]

            return True

        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
