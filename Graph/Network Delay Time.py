import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        max_delay = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            max_delay = max(max_delay, cost)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (cost + weight, neighbor))

        return max_delay if len(visited) == n else -1
