class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        lowest_price = prices[0]

        for i in range (1, len(prices)):
            if lowest_price > prices[i]:
                lowest_price = prices[i]
                
            else:
                day_profit = prices[i] - lowest_price
                total_profit += day_profit
                lowest_price = prices[i]
        
        return total_profit