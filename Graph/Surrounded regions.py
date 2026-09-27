class Solution:
    def solve(self, board: list[list[str]]) -> None:

        m = len(board)
        n = len(board[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c):
            board[r][c] = "S"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and board[nr][nc] == "O"
                ):
                    dfs(nr, nc)

        # 1. Mark all boundary-connected O's as safe
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][n - 1] == "O":
                dfs(r, n - 1)

        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)

            if board[m - 1][c] == "O":
                dfs(m - 1, c)

        # 2. Capture surrounded O's
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "S":
                    board[r][c] = "O"