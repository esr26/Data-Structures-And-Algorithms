class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            left = 0
            right = len(nums)-1
            res = -1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid
                    right = mid - 1

                elif nums[mid] > target:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            return res
        
        def findLast():
            left = 0
            right = len(nums)-1
            res = -1
            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            return res
        
        return [findFirst(), findLast()]


