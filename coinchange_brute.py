def coinchange(coins, amount):
    result = amount+1
    if amount == 0:
        return 0
    else:
        for coin in coins:
            if coin<=amount:
                result = min(result, coinchange(coins, amount-coin)+1)
        return result

print(coinchange([10,7,1], 14))