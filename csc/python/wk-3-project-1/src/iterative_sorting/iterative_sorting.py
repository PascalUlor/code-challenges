# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop
    # First pass
    # for i in range(0, len(arr) - 1):
    #     for j in range(0, len(arr)-1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Optimised version
    """
    1. create a boolean variable `noSwaps`
    2. start looping with variable i from end of array to begining of array and and set
    `noSwaps` to True in the loop
    3. start inner loop with variable j from begining of array to until (i-1)
    4. compare arr[j] with arr[j+1] and swap positions 
        if arr[j] > arr[j+1] and set `noSwaps` to False in the inner loop
    5. if `noSwaps` is still True `Break`
    6. return sorted array
    """
    noSwaps = True
    for i in range(len(arr) - 1, -1, -1):
        noSwaps
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                noSwaps = False
        if noSwaps:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    """
    Note upperbound of k is O(n) and it does not work with floats or negative values
    it can not also be applied on set of numbers with varied range
    count = array of k+1 zeros
    for x in input:
        count[key(x)] += 1

    total = 0
    for i in 0, 1, ... k:
        count[i], total = total, count[i] + total

    output = array of the same length as input
    for x in input:
        output[count[key(x)]] = x
    count[key(x)] += 1 

    return output
    """
    if len(arr) == 0:
        return arr
    # k is the maximum number in array
    # k + 1; // the length of the array containing counts
    maximum = max(arr)
    k = maximum
    # initialize count array // it stores counts with indexes from 0 to k-1
    count_array = [0]*(k+1)

    # populate count array using the count of each array value as its index
    for i in range(0, len(arr)):
        count_array[arr[i]] += 1

    print('==init==', count_array)

    # take cumulative sum from of each value in count array
    for i in range(1, k+1, 1):
        count_array[i] = count_array[i] + count_array[i-1]

    print('==final==', count_array)

   # initialize sorted/output array
    sorted_array = [0]*len(arr)

    # populate sorted array using the values from count array as its index and
    # placing the values from main array in each index.
    # decrement count array by 1 in each iteration
    for i in range(len(arr)-1, -1, -1):
        print('==final==', count_array[arr[i]], '=====', arr[i])
        count_array[arr[i]] -= 1
        sorted_array[count_array[arr[i]]] = arr[i]

    # set main array equal to sorted array
    for i in arr:
        if i < 0:
            sorted_array = 'Error, negative numbers not allowed in Count Sort'
    arr = sorted_array
    print('==final+++++==', sorted_array)

    return arr
