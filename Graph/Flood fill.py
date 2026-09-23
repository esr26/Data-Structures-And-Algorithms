from collections import deque

class Solution:
    def floodFill(
        self,
        image: list[list[int]],
        sr: int,
        sc: int,
        color: int
    ) -> list[list[int]]:

        original = image[sr][sc]

        if original == color:
            return image

        m, n = len(image), len(image[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and image[nr][nc] == original
                ):
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image