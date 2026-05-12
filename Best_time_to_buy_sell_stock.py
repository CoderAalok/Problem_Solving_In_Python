# def maxProfit(prices) -> int:
#     # Initillize price and profit
#     min_price = float('inf')
#     max_profit = 0
#     # continuously tracking minimum price
#     for price in prices:
#         # Approach - I
#         # Buying a stock
#         min_price = min(min_price, price)
#         # sell to calulating profit
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
        
#         # Approach - II
#         # if price < min_price:
#         #     min_price = price
#         # else:
#         #     profit = price - min_price
#         #     max_profit = max(max_profit, profit)
    
#     return max_profit

# prices = [5,6,3,9,1,10,50]
# print(maxProfit(prices))
