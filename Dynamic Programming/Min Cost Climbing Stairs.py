class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        step_1 = 0
        step_2 = 0

        for i in range(n - 1, -1, -1):
            current = cost[i] + min(step_1, step_2)
            step_2 = step_1
            step_1 = current

        return min(step_1, step_2)
