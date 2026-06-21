class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        n = len(heights)
        stack = []



        for idx, height in enumerate(heights):

            start = idx

            while stack and stack[-1][0] > height:

                h, i = stack.pop()

                w = idx - i

                max_area = max(max_area, h * w)

                start = i
            
            stack.append((height, start))
        
        while stack:

            h, i = stack.pop()

            max_area = max(max_area, h * (n-i))

        
        return max_area



            



        