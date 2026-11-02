from collections import defaultdict


class Solution:
    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:
        graph = defaultdict(list)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1.0 / value))

        def dfs(src: str, dst: str, product: float, visited: set[str]) -> float:
            if src == dst:
                return product

            visited.add(src)
            for neighbor, cost in graph[src]:
                if neighbor in visited:
                    continue

                result = dfs(neighbor, dst, product * cost, visited)
                if result != -1.0:
                    return result

            return -1.0

        answers = []
        for src, dst in queries:
            if src not in graph or dst not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(src, dst, 1.0, set()))

        return answers
