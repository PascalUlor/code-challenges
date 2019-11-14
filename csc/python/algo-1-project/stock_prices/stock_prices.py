#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # pass
  buying_price = prices[0]
  max_profit = prices[1] - buying_price
  for i in range(1, len(prices)):
    new_price_diff = prices[i] - buying_price
    if new_price_diff > max_profit:
      max_profit = new_price_diff
    if buying_price > prices[i]:
      buying_price = prices[i]
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))