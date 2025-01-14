class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i in range(n):
            curr = temperatures[i]
            while stack and stack[-1][1] < curr:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, curr))
        
        return ans
        