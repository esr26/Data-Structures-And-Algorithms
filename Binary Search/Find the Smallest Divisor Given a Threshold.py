class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int):

        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            curr = 0
            for num in nums:
                curr += (num + mid - 1) // mid

            if curr <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        return left
        