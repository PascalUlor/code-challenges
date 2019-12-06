"""
You are given  queries. Each query is of the form two integers described below:
(1,x) : Insert x in your data structure.
(2,y) : Delete one occurence of y from your data structure, if present.
(3,z) : Check if any integer is present whose frequency is exactly z.
If yes, print 1 else 0.
(query, data) pair
queries ==> (action, value)
"""

# Complete the freqQuery function below.

def binary_search(arr, target, low, high):
        mid = (low + high)//2
        if len(arr) == 0:
            return -1
        guess = arr[mid]
        if guess == target:
            return mid
        if guess < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
def freqQuery(queries):
    cache = []
    output = {}
    count = []
    for pair in queries:
        if pair[0] == 1:
            cache.append(pair[1])
        if pair[0] == 2 and len(cache) != 0:
            item = binary_search(cache, pair[1], 0, len(cache)-1)
            cache.pop(item)
        if pair[0] == 3:
            if len(cache) == 0:
                count.append(0)
            for i in cache:
                if i not in output:
                    output[i] = 1
                else:
                    output[i] += 1
            for j in output.values():
                if j == pair[1]:
                    count.append(1)
                else:
                    if 0 not in count:
                        count.append(0)
    print(output, 'output')
    print(cache, '==cache')
    print(count, 'count')
    return count


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
