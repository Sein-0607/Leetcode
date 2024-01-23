class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        n = len(prices)
        profit = 0
        min_price = max(prices) # 6
        
        for curr in prices:
            if curr < min_price:
                min_price = curr
                
            elif curr - min_price > profit:
                profit = curr - min_price
            
        return profit
      
