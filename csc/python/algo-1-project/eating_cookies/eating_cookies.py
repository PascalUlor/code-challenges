#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

"""
1. Given `n` = number of cookies and [0, 1, 2, 3] variations to eat cookies
2. from the possible variations [0, 1, 2, 3] we specify base cases
    Base Case: for variation zero (0) there is only 1 way to eat zero cookies i.e if n == 0 return 1
    and number of cookies can not be less than zero i.e if n < 0 return 0`
3. decrease n by variations 1, 2 and 3 till base case condition is met
4. Sum all variation results
"""


def eating_cookies(n, cache=None):
    # pass
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        print(cache[n])
        return cache[n]

# def eating_cookies(n):
#     variations_of_ways = [0, 1, 2, 3]
#     number_of_ways = [0] * (n + 1)

#     #set base case for number of ways to eat 0 cookies
#     number_of_ways[0] = 1
#     for ways_to_eat_cookies in range(1, len(variations_of_ways)):
#         for max_cookies_taken in range(ways_to_eat_cookies, n+1):
#             left_over = max_cookies_taken - ways_to_eat_cookies
#             number_of_ways[max_cookies_taken] += number_of_ways[left_over]
#     return number_of_ways[n]


print(eating_cookies(3))



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
