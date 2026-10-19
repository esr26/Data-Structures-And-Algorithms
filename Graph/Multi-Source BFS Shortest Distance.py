from collections import deque


class Solution:
    def shortestDistance(
        self,
        grid: list[list[str]],
        target_row: int,
        target_col: int,
    ) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])

        distance = [[-1] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "S":
                    queue.append((r, c))
                    distance[r][c] = 0

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and distance[nr][nc] == -1
                ):
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

        return distance[target_row][target_col]
