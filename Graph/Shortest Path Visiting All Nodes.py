from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1
        queue = deque()
        visited = set()

        for node in range(n):
            mask = 1 << node
            queue.append((node, mask, 0))
            visited.add((node, mask))

        while queue:
            node, current_mask, steps = queue.popleft()
            if current_mask == target_mask:
                return steps

            for neighbor in graph[node]:
                new_mask = current_mask | (1 << neighbor)
                state = (neighbor, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, new_mask, steps + 1))

        return -1
