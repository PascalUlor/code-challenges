# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    if len(arrA) == 0:
       return arrB
    elif len(arrB) == 0:
        return arrA

    index_left = index_right = 0
    list_merged = []
    while len(list_merged) < elements:
        if arrA[index_left] <= arrB[index_right]:
            list_merged.append(arrA[index_left])
            index_left += 1
        else:
            list_merged.append(arrB[index_right])
            index_right += 1

        if index_right == len(arrB):
            list_merged += arrA[index_left:]
            break
        elif index_left == len(arrA):
            list_merged += arrB[index_right:]
            break
        
    merged_arr = list_merged
    return merged_arr
    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        median = len(arr)//2
        left = arr[:median]
        right = arr[median: len(arr)]
        return merge(merge_sort(left), merge_sort(right))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
