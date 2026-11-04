class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit < 0:
                min_price = prices[i]
            max_profit = max(max_profit, profit)

        return max_profit

        #           0, 1, 2, 3
        # prices = [1, 2, 3, 4]
        # max_porfit = 3 units

        # prices = [2, 4, 3, 1]
        # lets assume the first day is the min
        # max_profit = 0

        # min_price = 2
        # curr_price = 1
        # max_profit = curr_pirce = min_price =n 1 - 2 = -1
        # max_profit = max between 0 and -1 = 0
        
        # if max_profit is < 0:
        #     set min_prcie to curr_price
        #     min_oprice = 1

        # next iteration:
        #     min_prioce = 1
        #     curr_price = 3
        #     max_profit = curr_price - min_price = 3 - 1 = 2
        #     if max_profit is < 0:
        #         set min_prcie to curr_price
        #         min_oprice = 1
        #     max_profit = max between 0 and 2 = 2


        # max_profit = curr_price - min_price = -1


        