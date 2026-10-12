import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        distance = {node: float('inf') for node in range(1, n + 1)}
        distance[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if cost > distance[node]:
                continue

            for neighbor, weight in graph[node]:
                new_distance = cost + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))

        if max(distance.values()) == float('inf'):
            return -1

        return max(distance.values())