"""
1. Sort the array. The selected packets must be a subarray of k elements
2. Take a subarray of m elements and assume we have calculated the sum of the elements to be s and the unfairness sum to be u
Imagine what would happen to s and u if we add the next element to the subarray
Imagine what would happen to s and u if we remove the first element of the subarray
And don't forget to use int64 or BigInt (for JS)
"""

# def angryChildren(k, packets):
#     packets.sort()
#     pck_sum =0
#     difference =0

#     for i in range(0,k):
#         difference += abs(packets[i]*(i) - pck_sum)
#         pck_sum += packets[i]

#     min_diff = difference
#     return min_diff
    # sorted_list = sorted(packets)
    # min_range = sorted_list[:k]
    # cum_diff = 0
    # for i in range(0,len(min_range)):
    #     for j in range(i+1, len(min_range)):
    #         cum_diff += abs(min_range[i] - min_range[j])
    # return cum_diff


def angryChildren(k, packets):
    packets.sort()
    print(packets)

    pck_sum =0
    difference =0

    for i in range(k-1,-1,-1):
        difference = difference + abs(packets[i]*(k-1 - i) - pck_sum)
        pck_sum = pck_sum + packets[i]

    min_diff = difference

    for j in range(k,len(packets)):
        pck_sum = pck_sum - packets[j-k]

        difference = difference - abs(pck_sum - packets[j-k]*(k-1))

        difference = difference + abs(pck_sum - (k-1)*packets[j])


        if(difference < min_diff ):
            min_diff = difference

        pck_sum = pck_sum + packets[j]
    
    return min_diff


print(angryChildren(3, [10, 100, 300, 200, 1000, 20, 30]))