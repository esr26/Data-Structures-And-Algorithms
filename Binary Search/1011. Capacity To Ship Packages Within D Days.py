class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)
        ans = 0

        while left <= right:
            mid = (left+right)//2

            total = 0
            d = 1
            for w in weights:
                if total + w <= mid:
                    total += w
                else:
                    d += 1
                    total = w
                    
            
            if d <= days:
                ans = mid
                right = mid-1
            else:
                left = mid + 1

        return ans




