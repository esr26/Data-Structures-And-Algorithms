class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)


        while left <= right:
            mid = (left + right) // 2

            subarray = 1
            curr = nums[0]

            for num in nums[1:]:
                if curr + num > mid:
                    subarray += 1
                    
                    curr = num
                
                else:
                    curr += num
            
            if subarray <= k:
                right = mid - 1
            
            else:
                left = mid + 1

        return left

