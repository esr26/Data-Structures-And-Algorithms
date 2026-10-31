import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])

        min_heap = [(0, (0, 0))]
        effort = [[float("inf")] * n for _ in range(m)]
        effort[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            w, (r, c) = heapq.heappop(min_heap)

            if w > effort[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return w

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(w, diff)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, (nr, nc)))

        return -1
