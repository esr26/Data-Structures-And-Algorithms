class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(start, end):
            dp = [0] * (n + 3)

            for i in range(end, start - 1, -1):
                dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

            return max(dp[start], dp[start + 1])

        # Case 1: Exclude the last house
        case1 = solve(0, n - 2)

        # Case 2: Exclude the first house
        case2 = solve(1, n - 1)

        return max(case1, case2)
