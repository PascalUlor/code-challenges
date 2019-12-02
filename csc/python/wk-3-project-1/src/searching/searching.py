# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
  # low and high to keep track of which
  # part of the list we are searching
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
    # guess the mid value
    midpoint = (low + high)//2
    guess = arr[midpoint]
    
    if guess < target:
      # shift value of low towards/after midpoint if guess is less that target
      low = midpoint + 1
    else:
      # shift value of high towards/after midpoint if guess is greater that target
      high = midpoint - 1
      # if target is at midpoint return midpoint
    if guess == target:
      return midpoint

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  guess = arr[middle]

  if guess == target:
    return middle
  if guess < target:
    return binary_search_recursive(arr, target, middle + 1, high)
  else:
    return binary_search_recursive(arr, target, low, middle - 1)
