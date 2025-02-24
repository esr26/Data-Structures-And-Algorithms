class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []

        for i in range(numRows):
            curr = [1]*(i+1)
            
            for j in range(1,i):
                curr[j] = res[-1][j]+res[-1][j-1]
            
            res.append(curr)
            
        return res

