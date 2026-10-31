from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0

        min_val = prices[0]

        for price in prices[1:]:

            min_val = min(price, min_val)

            profit = max(profit, price-min_val)
        
        return profit



            
