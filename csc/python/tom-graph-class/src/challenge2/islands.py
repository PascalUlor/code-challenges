# island count problem big hint (use a Stack)


# data structures (stack queue etc)
class Stack:
    def __init__(self):
        self.storage = []
    
    """ 
        Push method
        -----------
        takes in a value and appends it to the storage
    """
    def push(self, value):
        self.storage.append(value)

    """
        Pop Method
        ----------
        checks if there is data left 
        and returns the top of the stack storage
    """
    def pop(self):
        # check if storage has any data
        if self.size() > 0:
            # return the top of the storage stack
            return self.storage.pop()
        # otherwise
        else:
            # return None
            return None
    
    """
        Size Method
        -----------
        Returns the length of the storage list
    """
    def size(self):
        return len(self.storage)

# you can also just copy a stack from the other code
class OtherStack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# helper functions (traversal algorithm function bft, dft etc)
# (get neighbors, etc)

# example algorithm
def get_neighbors(x, y, matrix):
    # create a neighbors list
    # check the north south east and west for any 1's
    # (this would be a bunch of if conditions)
        # and append any positive finds 
        # to the neighbors list as a tuple

    #return neighbors


# a simple dfs / sft to deal with the nested lists


def dft(x, y, matrix, visited):
    # create a stack
    # push (x, y) tuple to the stack
    # while the stack has data
        # pop a vert off the stack
        # if the tuple is not in the visited structure
            # add the tuple to the visited structure
            # loop over each neighbor and run get_neighbor 
            # on vert[0] , vert[1] and the matrix
                # push the neighbor on to the stack
        # return visited


# main island counter function

def island_counter(matrix):
    # create a visited matrix
    # loop over the matrix
        # append False to the visited matrix 
        # times the length of the matrix[0]
    # set an island counter
    # loop over the x
        # loop over the y
            # check if [y][x] are visited
                # if the matrix at [y][x] are equal to 1
                    # set the visited to the dfs 
                    # passing in x, y, matrix and visited
                    # increment island count
                # otherwise
                    # set visited at [y][x] to True
    # return island count
    pass


if __name__ == '__main__':
    islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

    island_counter(islands)  # 4

    islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

    island_counter(islands)  # 13