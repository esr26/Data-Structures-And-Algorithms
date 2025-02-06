class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res = 0
        i = 0
        for j in range(len(nums)):

            if nums[j] == 0:
                res += (j-i+1)
            
            else: 
                i = j + 1
        return res

