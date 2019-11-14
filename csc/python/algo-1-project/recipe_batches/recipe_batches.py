#!/usr/bin/python

"""
1. Filter out recipe ingredient from ingredient dict
2. Divide equivalent items in both dict by each other and get `quotient`
3. Get Result
    a. If any quotient == 0 return zero
    b. If all quotient >= 1 return the minimum
"""

import math

def recipe_batches(recipe, ingredients): # O(n)
  # pass 
  cart = dict()
  batch = 0
  # check if all ingredient needed are availble for recipe
  recipe_keys = list(recipe.keys()) # O(1)
  ingredients_keys = list(ingredients.keys()) # O(1)
  if len(recipe_keys) != len(ingredients_keys):
    return batch # O(1)
  else:
    for (key, value) in recipe.items():# O(n)
    # Check if key is in recipe and add pair to new dictionary
      if key in list(recipe.keys()):
        qty = ingredients[key] // value #(1)
        cart[key] = qty #(1)
    batch = sorted(list(cart.values()))[0] #(n)
    # print(cart)
    return batch #(1)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))