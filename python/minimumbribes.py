# Complete the minimumBribes function below.
"""
1. Get number of people on queue
2. Check index of each person on queue
    a) if index+1 != person then it's a bride
3.Get number of bribes
    a) if person > (index+1) and person - (index + 1) == 1 => count as valid
    b) if person > (index+1) and person - (index + 1) == 2 => count as valid
    c) if person > (index+1) and person - (index + 1) > 2 => 'Too chaotic '
    d) if person < (index+1) => pass
4. if there's no chaos sum all valid counts else return 'Too chaotic'
"""


def minimumBribes(q):
    numberOfBribes = 0
    # numberOfBribesAnIndividualCanAfford = 2  # stated in question
    for i in range(len(q) - 1, 0, -1):
                # immediately you discover that the current state requires that
                # people be more corrupt than we originally assumed, 
                # we stop the process
        if numberOfBribes == -1:
            break

        # in as much as the the referenced individual was not bribed,
        # we continue searching for anybody that was bribed
        if q[i] > q[i-1]:
            continue
        else:
            indexOfCorruptIndividual = i-1
            for j in range(i - 1, i + 1):
                if j + 1 >= len(q):
                    break
                if q[j] > q[j+1]:
                    tmp = q[j]
                    q[j] = q[j+1]
                    q[j+1] = tmp
                    numberOfBribes += 1
                    indexOfCorruptIndividual = j + 1

            if indexOfCorruptIndividual + 1 >= len(q):
                continue
            elif q[indexOfCorruptIndividual] > q[indexOfCorruptIndividual + 1]:
                numberOfBribes = -1

    if numberOfBribes == -1:
        print("Too chaotic")
    else:
        print(numberOfBribes)
    # queue = q[:]
    # chaos = False
    # count = int(0)
    # n = len(queue)
    # for index, person in enumerate(queue):
    #     if index+1 != person and person - (index + 1) != 0 and person > (index + 1):
    #         if person > index+1 and person - (index + 1) == 1:
    #             count += int(1)
    #         if person > index+1 and person - (index + 1) == 2:
    #             count += int(2)
    #         if person > index+1 and person - (index + 1) > 2:
    #             chaos = True
    #     else:
    #         if (index + 1) >= n:
    #             continue
    #         elif person > queue[index + 1]:
    #             count += int((index + 1) - person)

    # bribes = 'Too chaotic' if chaos else count
    # print(bribes)


# minimumBribes([2, 1, 5, 3, 4])
# minimumBribes([2, 5, 1, 3, 4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
