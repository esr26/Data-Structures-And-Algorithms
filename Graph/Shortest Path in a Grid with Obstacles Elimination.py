from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        best = [[-1] * n for _ in range(m)]
        best[0][0] = k

        queue = deque([(0, 0, k, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, available, steps = queue.popleft()

            if r == m - 1 and c == n - 1:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_available = available - grid[nr][nc]
                    if new_available >= 0 and new_available > best[nr][nc]:
                        best[nr][nc] = new_available
                        queue.append((nr, nc, new_available, steps + 1))

        return -1
