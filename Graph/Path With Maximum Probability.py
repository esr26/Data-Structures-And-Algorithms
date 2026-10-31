import heapq
from collections import defaultdict


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = defaultdict(list)
        for (u, v), edge_prob in zip(edges, succProb):
            graph[u].append((edge_prob, v))
            graph[v].append((edge_prob, u))

        best_prob = [0.0] * n
        best_prob[start_node] = 1.0
        max_heap = [(-1.0, start_node)]

        while max_heap:
            negative_prob, node = heapq.heappop(max_heap)
            prob = -negative_prob

            if prob < best_prob[node]:
                continue

            if node == end_node:
                return prob

            for edge_prob, neighbor in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > best_prob[neighbor]:
                    best_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        return 0.0
