from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        queue = deque([0])
        visited = {0}
        reversals = 0

        while queue:
            node = queue.popleft()
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    reversals += cost
                    visited.add(neighbor)
                    queue.append(neighbor)

        return reversals
