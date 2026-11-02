from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        target_mask = 0

        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == "@":
                    start_r, start_c = r, c
                elif "a" <= cell <= "f":
                    target_mask |= 1 << (ord(cell) - ord("a"))

        queue = deque([(start_r, start_c, 0, 0)])
        visited = {(start_r, start_c, 0)}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, steps = queue.popleft()
            if mask == target_mask:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                cell = grid[nr][nc]
                if cell == "#":
                    continue

                new_mask = mask
                if "a" <= cell <= "f":
                    new_mask |= 1 << (ord(cell) - ord("a"))
                elif "A" <= cell <= "F" and not (mask & (1 << (ord(cell) - ord("A")))):
                    continue

                state = (nr, nc, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_mask, steps + 1))

        return -1
