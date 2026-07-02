class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0

        while i < n:

            if nums[i]-1 != i:

                correct = nums[i] - 1

                if nums[i] == nums[correct]:
                    return nums[i]
                
                nums[correct], nums[i] = nums[i], nums[correct]
            
            else:
                i += 1
               
        
        


        