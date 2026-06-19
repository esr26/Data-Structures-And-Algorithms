class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)

        stack = []

        for idx, num in enumerate(temperatures):

            while stack and stack[-1][0] < num:

                _, i = stack.pop()

                ans[i] = idx - i

            
            stack.append([num, idx])
        
        return ans