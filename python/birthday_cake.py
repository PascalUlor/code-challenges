def birthday(s, d, m):
    """
    1. slice the array elements taking m at a time
    2. sum array slice of length m
    3. set up a counter
    3. if sum === d increment counter
    4. else go take another array slice of length m starting from index of previous slice
    """
    if len(s) == 0:
        return 0

    if sum(s[:m]) == d:
        return 1 + birthday(s[1:], d, m)
    else:
        return 0 + birthday(s[1:], d, m)

m = 2 #mo
d = 3 #day
print(birthday([1, 2, 1, 3, 2], d, m))

# arr = [1, 2, 1, 3, 2]
# print(arr.__le__([4]))