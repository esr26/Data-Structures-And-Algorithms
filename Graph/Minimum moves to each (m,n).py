

m, n = len(grid), len(grid[0])

if grid[0][0] == 1 or grid[m-1][n-1] == 1:
    return -1

distance = [[-1] * n for _ in range(m)]

queue = deque([(0, 0)])

distance[0][0] = 0
directions = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]

while queue:
    r, c = queue.popleft()

    

    for dr, dc in directions:
        nr, nc = dr + r, dc + c

        if 0 <= nr < m and 0 <= nc < n and distance[nr][nc] == -1 and grid[nr][nc] == 0:
            distance[nr][nc] = distance[r][c] + 1
            queue.append((nr, nc))

    if distance[m-1][n-1] != -1:
        return distance[m-1][n-1]

return -1

        

