from collections import deque


class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        indegree = [0] * n

        for neighbor in edges:
            if neighbor != -1:
                indegree[neighbor] += 1

        queue = deque(i for i in range(n) if indegree[i] == 0)

        while queue:
            node = queue.popleft()
            neighbor = edges[node]
            if neighbor != -1:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        longest = -1
        visited = set()

        for node in range(n):
            if indegree[node] > 0 and node not in visited:
                count = 0
                current = node
                while current not in visited:
                    visited.add(current)
                    count += 1
                    current = edges[current]
                longest = max(longest, count)

        return longest
