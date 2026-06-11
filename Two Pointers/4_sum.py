class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []
        n = len(nums)


        for i in range(n):

            if i > 0 and nums[i-1]==nums[i]:
                continue

            for j in range(i+1, n):

                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total > target:

                        right -= 1

                    elif total < target:
                        left += 1
                    
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left-1] == nums[left]:
                            left += 1
                        
                        while left < right and nums[right+1] == nums[right]:
                            right -= 1
        
        return res


        