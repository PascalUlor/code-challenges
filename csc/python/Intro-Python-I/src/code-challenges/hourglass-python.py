"""
1. loop over 1st 4 arrays
2. loop over 1st 4 elements in each array
3. get hourglass sums
    a. sum top row for hourglass
    b. sum middle row for hourglass
    c. sum bottom row of hourglass
4. set max sum
5. return max sum
"""


def hourglassSum(arr):
    hourglass_sums = []
    for i in range(0, 4):
        for j in range(0, 4):
            # top row
            s1 = arr[i][j]
            s2 = arr[i][j+1]
            s3 = arr[i][j+2]

            # middle row
            s4 = arr[i+1][j+1]

            # bottom row
            s5 = arr[i+2][j]
            s6 = arr[i+2][j+1]
            s7 = arr[i+2][j+2]
            total = s1+s2+s3+s4+s5+s6+s7
            hourglass_sums.append(total)
    maxValue = max(hourglass_sums)
    return maxValue


hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
])

# hourglassSum([
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 9, 2, -4, -4, 0],
#     [0, 0, 0, -2, 0, 0],
#     [0, 0, -1, -2, -4, 0]
# ])
