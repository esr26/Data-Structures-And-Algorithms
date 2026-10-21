from collections import defaultdict
import heapq


class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v, weight in connections:
            graph[u].append((weight, v))
            graph[v].append((weight, u))

        visited = set()
        min_heap = [(0, 1)]
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
