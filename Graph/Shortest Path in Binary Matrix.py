class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1

        dist[0][0] = 1
        heap = [(1, (0, 0))]

        directions = [
            (1, 1), (0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1),
            (-1, 1), (1, -1)
        ]

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node[0]][node[1]]:
                continue
            
            if node[0] == m - 1 and node[1] == n - 1:
                return d
            


            for dr, dc in directions:
                nr, nc = dr + node[0], dc + node[1]

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    new_dist = d + 1
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, (nr, nc)))
        
        return -1




        

        