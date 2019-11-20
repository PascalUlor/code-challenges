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
"""
Approach:
Maintain two pointers which point to start of the segments which have to be merged.
Compare the elements at which the pointers are present.
If element1 < element2 then element1 is at right position, simply increase pointer1.
Else place element2 in its right position and all the elements 
at the right of element2 will be shifted right by one position.
Increment all the pointers by 1.
"""
# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
# Inplace Implementation 
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # get a second start point from mid-point
    start2 = mid + 1

    # If the direct merge is already sorted return
    if arr[mid] < arr[start2]:
        return
    
# Two pointers to maintain start
# of both arrays to merge
    while start <= mid and start2 <= end:
        # element 1 = arr[start]
        # element 2 = arr[start2]
        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
      
                # Shift all the elements between element 1 
                # element 2, right by 1. (Swap)
            while index != start: 
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value 
      
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1
    return arr

"""
l is for left index and r is right index of the  
sub-array of arr to be sorted
"""
def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        median = int(l + (r - l) / 2)
        #Sort first and second halves 
        merge_sort_in_place(arr, l, median)
        merge_sort_in_place(arr, median + 1, r)
        merge_in_place(arr, l, median, r)

    return arr

# def merge_in_place(A,start,mid,end):
#     L = A[start:mid]
#     R = A[mid:end]
#     i = 0
#     j = 0
#     # k = start
#     for k in range(start,end):
#         if j >= len(R) or (i < len(L) and L[i] < R[j]):
#             A[k] = L[i]
#             i = i + 1
#         else:
#             A[k] = R[j]
#             j = j + 1
#     return A 

# def merge_sort_in_place(A,p,r):
#     if r - p > 1:
#         mid = int((p+r)/2)
#         merge_sort_in_place(A,p,mid)
#         merge_sort_in_place(A,mid,r)
#         merge_in_place(A,p,mid,r)
#     return A


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
