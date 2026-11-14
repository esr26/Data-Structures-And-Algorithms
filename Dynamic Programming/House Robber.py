class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # dp[i] is the best total when house i is robbed.
        dp = [0] * n
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]

        for i in range(n - 3, -1, -1):
            if i + 3 < n:
                dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
            else:
                dp[i] = nums[i] + dp[i + 2]

        return max(dp[0], dp[1])
