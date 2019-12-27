# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    abs_diff = []
    for i in range(0, len(arr)+1):
        start = arr[0]
        diff = start - arr[i]
        abs_diff.append(abs(diff))
        if len(arr) > 0:
            arr = arr[i+1:]
            continue
    print(sorted(abs_diff)[0])
    return sorted(abs_diff)[0]
    # abs_diff = []
    # for i in range(0, len(arr)):
    #     for j in range(0, len(arr)):
    #         if i != j:
    #             print(arr[i], arr[j])
    #             diff = arr[i] - arr[j]
    #             abs_diff.append(abs(diff))
        
    # print(sorted(abs_diff)[0])
    # return sorted(abs_diff)[0]


minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75])
# minimumAbsoluteDifference([3, -7, 0])
