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
    queue = q[:]
    chaos = False
    count = int(0)
    n = len(queue)
    for index, person in enumerate(queue):
        if index+1 != person and person - (index + 1) != 0 and person > (index + 1):
            if person > index+1 and person - (index + 1) == 1:
                count += int(1)
            if person > index+1 and person - (index + 1) == 2:
                count += int(2)
            if person > index+1 and person - (index + 1) > 2:
                chaos = True
        else:
            if (index + 1) > n:
                n = (index)
            else:
                if person < (index + 1) and (index + 1) >= (n + 1):
                    count += int((index + 1) - person)
    
    bribes = 'Too chaotic' if chaos else count
    print(bribes)

minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])