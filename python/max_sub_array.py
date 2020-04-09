arr = [2, -1, 2, 3, 4, -5]
arr2 = [-2, -3, -1, -4, -6]

# print(arr[0:-2])

def maxSubarray(arr):
    arr1 = arr[:]
    arr2 = sorted(arr[:])
    max_sub_arr = sum(arr1)
    max_sub_sq = sum(arr2)
    for i in range(0, len(arr1)):
        arr_sum_for = sum(arr1[i:])
        arr_sum_rev = sum(arr[0:-i])
        arr_sum = max(arr_sum_for, arr_sum_rev)
        if max_sub_arr < arr_sum:
            max_sub_arr = arr_sum
    for k in range(0, len(arr2)):
        arr_sum = sum(arr2[k:])
        if max_sub_sq < arr_sum:
            max_sub_sq = arr_sum
    if max(arr) < 0:
        max_sub_sq, max_sub_arr = max(arr), max(arr)
        return [max_sub_arr, max_sub_sq]
    else:
        return [max_sub_arr, max_sub_sq]


print(maxSubarray(arr2))