class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        if n == 0: return [-1, -1]

        left, right = 0, n-1
        while left <= right:

            mid = (left + right)//2

            if nums[mid] == target:
                left = right = mid
                while left >=0 and nums[left]==target :
                    left -= 1
                
                while right < n and nums[right]==target:
                    right += 1
                
                return [left+1, right-1]
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return [-1, -1]


        