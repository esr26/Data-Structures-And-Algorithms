import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        best = [[float("inf")] * n for _ in range(m)]
        best[0][0] = grid[0][0]
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            cost, r, c = heapq.heappop(min_heap)
            if cost > best[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = max(cost, grid[nr][nc])
                    if new_cost < best[nr][nc]:
                        best[nr][nc] = new_cost
                        heapq.heappush(min_heap, (new_cost, nr, nc))

        return -1
