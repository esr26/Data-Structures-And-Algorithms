class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1

        while row < m and col >= 0:

            curr = matrix[row][col]

            if curr == target:
                return True
            
            elif curr > target:
                col -= 1
            
            else:
                row += 1
        
        return False

    