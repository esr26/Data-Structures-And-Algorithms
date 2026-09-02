from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        queue = deque()

        # Add all boundary O's
        for r in range(m):
            if board[r][0] == "O":
                queue.append((r, 0))
                board[r][0] = "S"

            if board[r][n - 1] == "O":
                queue.append((r, n - 1))
                board[r][n - 1] = "S"

        for c in range(n):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "S"

            if board[m - 1][c] == "O":
                queue.append((m - 1, c))
                board[m - 1][c] = "S"

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # BFS from all boundary O's
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and board[nr][nc] == "O"
                ):
                    board[nr][nc] = "S"
                    queue.append((nr, nc))

        # Final conversion
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

                    