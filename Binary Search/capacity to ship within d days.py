class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)


        while left <= right:

            mid = (left + right) // 2

            day = 1
            load = 0

            for w in weights:
                if load + w <= mid:
                    load += w
                
                else:
                    load = w
                    day += 1

            if day <= days:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return left




        