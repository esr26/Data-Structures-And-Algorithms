class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[left] >= nums[mid]:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            
            elif nums[mid] > nums[right]:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid
            else:
                return nums[left]
        return nums[left]


        