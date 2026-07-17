class Solution:
    def findTwoElement(self, nums, n):
        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6

        actual_sum = sum(nums)
        actual_sq_sum = sum(x * x for x in nums)

        # x = repeating, y = missing
        diff = actual_sum - expected_sum              # x - y
        sq_diff = actual_sq_sum - expected_sq_sum     # x² - y²

        sum_xy = sq_diff // diff                      # x + y

        repeating = (diff + sum_xy) // 2
        missing = repeating - diff

        return [repeating, missing]
    
    