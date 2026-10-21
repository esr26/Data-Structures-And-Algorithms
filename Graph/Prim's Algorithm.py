import heapq


class Solution:
    def prim(self, n: int, edges: list[list[int]]) -> int:
        if n == 0:
            return 0

        graph = [[] for _ in range(n)]

        for u, v, weight in edges:
            graph[u].append((weight, v))
            graph[v].append((weight, u))

        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0

        while min_heap:
            weight, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += weight

            for edge_weight, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (edge_weight, nei))

        return total_cost if len(visited) == n else -1
