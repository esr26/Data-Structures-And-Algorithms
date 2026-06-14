class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float('inf')

        left = right = 0
        curr = 0

        while right < len(nums):

            curr += nums[right]

            while curr >= target and left <= right:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1
            
            right += 1
        
        return 0 if res == float('inf') else res
        