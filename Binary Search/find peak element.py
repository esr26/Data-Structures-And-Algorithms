class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # We are going uphill →
                # A peak exists on the right
                left = mid + 1

            else:
                # We are going downhill ←
                # mid itself could be the peak
                right = mid

        return left
    