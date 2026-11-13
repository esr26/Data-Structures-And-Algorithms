from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        def dfs(node, product):
            visited.add(node)
            if node == destination:
                return product

            for neighbor, weight in graph[node]:
                if neighbor in visited:
                    continue

                answer = dfs(neighbor, product * weight)
                if answer != -1.0:
                    return answer

            return -1.0

        graph = defaultdict(list)
        for i, (numerator, denominator) in enumerate(equations):
            value = values[i]
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1.0 / value))

        result = []
        for source, destination in queries:
            visited = set()
            if source not in graph or destination not in graph:
                result.append(-1.0)
                continue

            result.append(dfs(source, 1.0))

        return result
