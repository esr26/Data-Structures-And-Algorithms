class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        directions = [
            (1, 0, "D"),
            (-1, 0, "U"),
            (0, 1, "R"),
            (0, -1, "L")
        ]

        visited = set()
        shapes = set()

        def dfs(r, c, path):
            visited.add((r, c))

            for dr, dc, move in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and grid[nr][nc] == 1
                    and (nr, nc) not in visited
                ):
                    path.append(move)
                    dfs(nr, nc, path)

                    # Backtracking
                    path.append("B")

        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1 and (r, c) not in visited:

                    path = ["S"]   # starting point
                    dfs(r, c, path)

                    shapes.add(tuple(path))

        return len(shapes)