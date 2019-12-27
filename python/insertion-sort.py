"""
mark first element as sorted
loop through unsorted array from index 1 to len(array)
    'extract' the element X at index i as currentValue
    set j = i - 1 (which is the last Sorted Index)
    while index of sorted array j >= 0 and element of sorted array arr[j] > currentValue
        move sorted element to the right by 1
        decrement last Sorted Index j by 1
    else break loop and insert currentValue at arr[j + 1] in sorted  array
"""

def insertionSort(arr):
    for i in range(1, len(arr)):
        currentVal = arr[i] # 'extract' the element X at index i as currentValue
        j = i - 1 # set j = i - 1 (which is the last Sorted Index)
        while j >= 0 and arr[j] > currentVal:
            arr[j+1] = arr[j]
            j -= 1 # decrement last Sorted Index j by 1
        arr[j+1] = currentVal # insert currentValue at arr[j + 1] in sorted  array
    print(arr)
    return arr

insertionSort([2,1,9,76,4])