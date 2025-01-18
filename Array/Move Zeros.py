class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 1
        n = len(nums)
        while j < n:
            if nums[i] == 0 and nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            
            else:
                i += 1
                j += 1
        
        return nums
        