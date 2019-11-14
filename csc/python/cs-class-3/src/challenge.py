
 # chalenge. What is the complexity of this algorithm?
 """ Getting the time complexity of an iterative solution
- Compute the Big-O for each line in isolation.
- If something is in a loop, multiply it's Big-O by the loop for the total.
- If two things happen sequentially, add the Big-Os.
- Drop leading multiplicative constants from each Big-O.
- From all the Big-Os that are added, drop all but the biggest, dominating one."""

def complex_algo(items):

    for _ in range(5): # O(n)
        print ("Python is awesome") # O(c)

    for item in items: # O(n)
        print(item) # O(c)

    for item in items: # O(n)
        print(item) # O(c)

    print("Big O") # O(c)
    print("Big O") # O(c)
    print("Big O") # O(c)

complex_algo([4, 5, 6, 8])

# O(n) * O(c) => O(n)
# Linear