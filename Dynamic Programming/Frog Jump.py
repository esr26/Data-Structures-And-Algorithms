class Solution:
    def frogJump(self, heights: list[int]) -> int:
        n = len(heights)
        if n == 1:
            return 0

        dp = [0] * n
        dp[1] = abs(heights[0] - heights[1])

        for i in range(2, n):
            one_step = dp[i - 1] + abs(heights[i] - heights[i - 1])
            two_steps = dp[i - 2] + abs(heights[i] - heights[i - 2])
            dp[i] = min(one_step, two_steps)

        return dp[-1]
