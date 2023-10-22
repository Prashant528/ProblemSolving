def coinchange(coins, amount, cache={0:0}):
    print("Amount = ", amount)
    result = amount+1
    if amount in cache:
        print("Used cache for ", amount)
        return cache[amount]
    else:
        for coin in coins:
            if amount>=coin:
                result = min(result, coinchange(coins, amount-coin, cache)+1)
                cache[amount] = result
                print(cache)
        return result
    
print(coinchange([10,7,1], 14))