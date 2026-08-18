class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        left = 0
        right = n - 1

        while left <= right:

            mid = (left + right) // 2

            # Find maximum element in column mid
            max_row = 0

            for row in range(1, m):
                if mat[row][mid] > mat[max_row][mid]:
                    max_row = row

            # Check left neighbor
            left_val = mat[max_row][mid - 1] if mid > 0 else -1

            # Check right neighbor
            right_val = mat[max_row][mid + 1] if mid < n - 1 else -1

            curr = mat[max_row][mid]

            # Peak found
            if curr > left_val and curr > right_val:
                return [max_row, mid]

            # Right neighbor is bigger
            elif right_val > curr:
                left = mid + 1

            # Left neighbor is bigger
            else:
                right = mid - 1

        return [-1, -1]

    