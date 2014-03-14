def count(number, coin):
   number -= number % coin
   return number // coin

def calculate_coins(sum):
    total = sum * 100
    coins = [100, 50, 20, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        coin_count = count(total, coin)
        result[coin] = coin_count
        total -= coin_count * coin
    return result