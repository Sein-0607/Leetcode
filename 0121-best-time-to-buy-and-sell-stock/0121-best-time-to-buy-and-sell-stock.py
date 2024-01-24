class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return profit
        

        # 논리적이지 않은 풀이 
        # n = len(prices)
        # profit = 0
        # min_price = max(prices) # 6
        
        # for curr in prices:
        #     if curr < min_price:
        #         min_price = curr
                
        #     elif curr - min_price > profit:
        #         profit = curr - min_price
            
        # return profit
      
