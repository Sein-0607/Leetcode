class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)): # day2부터 수익계산 시작
            # i날의 수익
            day_profit = prices[i] - min_price
            if max_profit < day_profit:
                max_profit = day_profit
            # 새로운 조건 
            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit
        


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:      
#         profit = 0
#         min_price = prices[0]
        
#         for i in range(1, len(prices)):
#             profit = max(profit, prices[i]-min_price)
#             min_price = min(min_price, prices[i])
#         return profit
        

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
      
