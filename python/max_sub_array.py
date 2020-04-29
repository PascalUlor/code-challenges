arr = [2, -1, 2, 3, 4, -5]
arr2 = [-2, -3, -1, -4, -6]
leet = [-2,1,-3,4,-1,2,1,-5,4]

# print(arr[0:-2])

# def maxSubArray(arr):
#     arr1 = arr[:]
#     arr2 = sorted(arr[:])
#     max_sub_arr = sum(arr1)
#     max_sub_sq = sum(arr2)
#     for i in range(0, len(arr1)):
#         arr_sum_for = sum(arr1[i:])
#         arr_sum_rev = sum(arr[0:-i])
#         arr_sum = max(arr_sum_for, arr_sum_rev)
#         if max_sub_arr < arr_sum:
#             max_sub_arr = arr_sum
#     for k in range(0, len(arr2)):
#         arr_sum = sum(arr2[k:])
#         if max_sub_sq < arr_sum:
#             max_sub_sq = arr_sum
#     if max(arr) < 0:
#         max_sub_sq, max_sub_arr = max(arr), max(arr)
#         return [max_sub_arr, max_sub_sq]
#     else:
#         return [max_sub_arr, max_sub_sq]

def maxSubarray(arr): #hackerrank
    arr1 = arr[:]
    arr2 = sorted(arr[:])
    max_sub_arr = float('-inf')
    max_sub_sq = float('-inf')
    current_sum = 0
    current_sum2 = 0
    for x in arr1:
        current_sum = max(x, current_sum + x)
        max_sub_arr = max(max_sub_arr, current_sum)
    for k in arr2:
        current_sum2 = max(k, current_sum2 + k)
        max_sub_sq = max(max_sub_sq, current_sum2)
    if max(arr) < 0:
        max_sub_sq, max_sub_arr = max(arr), max(arr)
        return [max_sub_arr, max_sub_sq]
    else:
        return [max_sub_arr, max_sub_sq]n max_sub_arr

def maxSubArray(numbers): #leetcode
    largest_sum = float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        largest_sum = max(largest_sum, current_sum)
    return largest_sum


print(maxSubArray(leet))