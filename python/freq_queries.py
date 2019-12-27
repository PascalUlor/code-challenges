"""
You are given  queries. Each query is of the form two integers described below:
(1,x) : Insert x in your data structure.
(2,y) : Delete one occurence of y from your data structure, if present.
(3,z) : Check if any integer is present whose frequency is exactly z.
If yes, print 1 else 0.
(query, data) pair
queries ==> (action, value)
"""
# defaultdict is an inbuilt obj with preset keys

# Complete the freqQuery function below.
from collections import defaultdict
def freqQuery(queries):
    val_count = defaultdict(int) # key value pair of the each number and the number of times they appear
    freq_count = defaultdict(int) # key value pair of the freq of each numbers and the count of numbers with that freq
    result = []

    for i, j in queries:
        if i == 1:
            # check if j is in val_count object
            if j in val_count:
                # if j is already in val_count then on incrementing
                # the count of j in val_count we must decrement the count of 
                # numbers with the old freq of j
                if freq_count[val_count[j]] > 0:
                    freq_count[val_count[j]] -= 1
                # then increment the count of j in val_count and freq in freq_count
                val_count[j] += 1
                freq_count[val_count[j]] += 1
            else:
                # if j has never been counted in val_count we add it and count
                val_count[j] = 1
                if freq_count[val_count[j]]:
                    freq_count[val_count[j]] += 1
                else:
                    freq_count[val_count[j]] = 1
        if i == 2:
            if val_count[j]:
                # decrement old count
                freq_count[val_count[j]] -= 1
                val_count[j] -= 1
                # increment new count
                freq_count[val_count[j]] += 1
        if i == 3:
            # since we are searching for values that appear j times
            if j in freq_count and freq_count[j] > 0:
                result.append(1)
            else:
                result.append(0)
    return result

arr = [(1, 5),
 (1, 6),
 (3, 2),
 (1, 10),
 (1, 10),
 (1, 6),
 (2, 5),
 (3, 2)]
arr2 = [
    (3, 4),
    (2, 1003),
    (1, 16),
    (3, 1)
    ]
freqQuery(arr2)
freqQuery(arr)
