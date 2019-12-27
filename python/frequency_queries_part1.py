from collections import defaultdict

def freqQuery(queries):
    # reference to the item we want to get 
    # use an object with keys as ints and values as frequencies 
    obj = defaultdict(int)
    answers = []

    # loop over all of the queries in the queries array
    for i, j in queries:
        # if we see a 1 query
        if i == 1:
            # if the value is in the object 
            # O(1)
            if j in obj:
                # increment its frequency count
                obj[j] += 1
            # if its not in the object
            else:
                # add it and set its frequency to 1 
                obj[j] = 1
        # if we see a 2 query
        if i == 2:
            # O(1)
            # check if the value exists in our object 
            if j in obj and obj[j] > 0:
            # if it does, decrement its frequency by 1 
                obj[j] -= 1
        # if we see a 3 query 
        if i == 3:
            # O(n) linear in the number of key, value pairs 
            if j in obj.values():
                answers.append(1)
            else:
                answers.append(0)
            # check if any of the frequencies matches the 
            # value in the query 
            # the only to do that with a single object is to 
            # loop over every element in the object and check
            # its value   
        
    return answers