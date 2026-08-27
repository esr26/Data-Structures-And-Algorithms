class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2:
                    queue.append((i, j))
                
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0

        directions = [[0,1], [1,0], [-1, 0], [0,-1]]

        while queue and fresh > 0:

            for _ in range(len(queue)):

                row, col = queue.popleft()

                for r, c in directions:
                    nr = row + r
                    nc = col + c

                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc]==1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1 

                
        
        