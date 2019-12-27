# Complete the maximumToys function below.
"""
1. sort price list
2. loop through price list for prices <= cash
3. if price is <=  cash add to cart
"""


def maximumToys(prices, k):
    count = 0
    sum = 0
    price_list = sorted(prices)
    for i in price_list:
        if sum + i <= k:
            sum += i
            count += 1
        else:
            return count


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 7))
