from collections import deque


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        queue = deque([(0, 0)])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        while queue:
            r, c = queue.popleft()

            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    cost = 0 if grid[r][c] == i + 1 else 1
                    new_dist = dist[r][c] + cost

                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist

                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))

        return dist[m - 1][n - 1]
