class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        min_val = prices[0]

        for price in prices[1:]:

            min_val = min(price, min_val)

            profit = max(profit, price-min_val)
        
        return profit



            
