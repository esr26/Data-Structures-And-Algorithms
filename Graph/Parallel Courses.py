from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = defaultdict(list)
        completed = 0
        minimum = 0
        queue = deque()
        indegree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        for node in range(1, n + 1):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            minimum += 1

            for _ in range(len(queue)):
                node = queue.popleft()
                completed += 1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return minimum if completed == n else -1
