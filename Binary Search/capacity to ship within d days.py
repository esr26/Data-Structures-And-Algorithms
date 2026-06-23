class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left+right)//2

            day = 1
            curr_w = 0

            for w in weights:
                if curr_w + w > mid:
                    day += 1
                    curr_w = w
                
                else:
                    curr_w += w    
                    
                
            
            if day <= days:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return left
        