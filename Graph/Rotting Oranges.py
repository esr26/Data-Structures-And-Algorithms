from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        queue = deque()

        minutes = 0
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:
            rotted = False

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        rotted = True

            if rotted:
                minutes += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return minutes
