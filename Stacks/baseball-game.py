class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []


        for s in operations:

            if s == "C" and stack:
                stack.pop()
            
            elif s == "D" and stack:
                stack.append(stack[-1]*2)
            
            elif s == "+" and stack:
                stack.append(stack[-1] + stack[-2])
            
            else:
                stack.append(int(s))
        
        return sum(stack)
            



