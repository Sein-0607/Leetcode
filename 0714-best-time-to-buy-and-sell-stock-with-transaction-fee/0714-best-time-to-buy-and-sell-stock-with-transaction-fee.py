class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        total_profit = 0
        min_price = prices[0]
        # fee는 거리할때마다 내는 수수료 개념

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

             
            if prices[i] > min_price:
                day_profit = prices[i] - min_price - fee
                if day_profit > 0: # 수익이 있을 경우에만 저장
                    total_profit += day_profit
                    # 수익을 냈을 경우, 다시 사야 함. (min_price 갱신)
                    min_price= prices[i] - fee

        return total_profit
