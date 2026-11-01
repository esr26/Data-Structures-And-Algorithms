from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, available, steps = queue.popleft()

            if r == m - 1 and c == n - 1:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_available = available - grid[nr][nc]
                    state = (nr, nc, new_available)

                    if new_available >= 0 and state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, new_available, steps + 1))

        return -1
