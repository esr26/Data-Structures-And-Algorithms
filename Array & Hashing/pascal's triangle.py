class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1] for _ in range(numRows)]

        for row in range(1, numRows):

            for i in range(1, row):

                res[row].append(res[row-1][i] + res[row-1][i-1])
            
            res[row].append(1)
        
        return res
