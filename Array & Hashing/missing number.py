class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):

            while 0 <= nums[i] <= n - 1 and nums[i] != i:

                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        

        for i in range(n):

            if i != nums[i]:
                return i
            
        
        return n
        