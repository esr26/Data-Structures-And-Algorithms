from collections import deque


def minimum_moves(grid):
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return -1

    distance = [[-1] * n for _ in range(m)]
    distance[0][0] = 0
    queue = deque([(0, 0)])
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while queue:
        r, c = queue.popleft()
        if r == m - 1 and c == n - 1:
            return distance[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and distance[nr][nc] == -1 and grid[nr][nc] == 0:
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))

    return -1
