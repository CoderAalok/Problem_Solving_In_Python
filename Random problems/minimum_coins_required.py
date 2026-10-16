def minimum_coins(amount: int, coins: list[int]):
    total_coins = {}
    i = 0
    x = amount
    
    # break given amount
    while x != 0:
        # collect number of coins
        total_coins[coins[i]] = x // coins[i]
        # update amount
        x %= coins[i]
        i += 1
    
    return total_coins

# test
amount = 1000
coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]

result = minimum_coins(amount, coins).items()
total_coins = 0

for coin, i in result:
    if i != 0:
        print(f"{coin} * {i},", end="  ")
        total_coins += i
        

print(f"\nTotal no. coins = {total_coins}")
