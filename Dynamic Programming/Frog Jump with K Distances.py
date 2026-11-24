class Solution:
    def frogJump(self, heights: list[int], k: int) -> int:
        n = len(heights)
        if n <= 1:
            return 0

        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(1, n):
            for jump in range(1, min(k, i) + 1):
                energy = dp[i - jump] + abs(heights[i] - heights[i - jump])
                dp[i] = min(dp[i], energy)

        return dp[-1]
