class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c):
            grid[r][c] = "0"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and grid[nr][nc] == "1"
                ):
                    dfs(nr, nc)

        count = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count