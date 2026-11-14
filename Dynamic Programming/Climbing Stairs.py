class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def f(steps):
            if steps in memo:
                return memo[steps]

            memo[steps] = f(steps - 1) + f(steps - 2)
            return memo[steps]

        return f(n)
