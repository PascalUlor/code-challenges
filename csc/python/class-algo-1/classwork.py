def bar(n):
        s = 0 # O(1)

        for i in range(n): #O(n)
            for j in range(n): #O(n)
                s += i * j #O(1)
        return s #O(1)

        #O(n+n^2)
# Work out the time complexity of these solutions

"""
Formally:
1. Compute the Big-O for each line in isolation
2. if something is in a loop, multiply it's Big-O by the loop for the total.
3. If two things happen sequentially, add the Big-Os.
4. Drop leading multiplicative constants from each of the Big-Os.
5. From all of the Big-Os that are added, drop all but the biggest, dominating one.
"""

# 1
def baz(n):
    s = 0 #O(1)

    for i in range(n): #(n)
        for j in range(int(sqrt(n))): # n * sqrt(n) => O(sqrt(n)*n)
            s += i * j # O(1)
    
    return s #O(1)

    """
    3*O(1) + O(n) + O(sqrt(n)*n) => O(sqrt(n)*n)
    """

# 2
def frotz(n):
    s = 0 #O(1)

    for i in range(n): #O(n)
        for j in range(2 * n): # n * 2n => O(2n^2) => O(n^2)
            s += i * j #O(1)

    return s #O(1)

    """
    3*O(1) + O(n) + O(n^2) => O(n^2)
    """

# 3
def bar(x):
    sum = 0 #O(1)
    for i in range(0, 1463): O(n)
        i += sum # n * 1
        for _ in range(0, x): # n * n => O(n^2)
            for _ in range(x, x + 15): # n * n * n => O(n^3)
                sum += 1 # n * n * n => O(n^3) * 1

    """
    n * 1 + O(n^2) + O(n^3) + O(n^3) => O(n^2)
    """