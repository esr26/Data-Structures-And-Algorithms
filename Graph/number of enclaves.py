class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:

        def dfs(r, c):

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    dfs(nr, nc)


        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for c in range(n):
            if grid[0][c] == 1:
                grid[0][c] = 2
                dfs(0, c)

            if grid[m - 1][c] == 1:
                grid[m - 1][c] = 2
                dfs(m - 1, c)

        for r in range(1, m - 1):
            if grid[r][0] == 1:
                grid[r][0] = 2
                dfs(r, 0)

            if grid[r][n - 1] == 1:
                grid[r][n - 1] = 2
                dfs(r, n - 1)

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
        
        return count


        