https://www.hackerrank.com/challenges/count-luck/problem
class Stack():
    def __init__(self):
        self.Stack = []
    def push(self, value):
        self.Stack.append(value)
    def pop(self):
        if self.size():
            return self.Stack.pop()
        else:
            return None
    def size(self):
        return len(self.Stack)
# Complete the countLuck function below.
def countLuck(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    sr = None
    sc = None
    fr = None
    fc = None
    path = None
    neighbours = {}
    counter = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'M':
                sr = row
                sc = col
            elif matrix[row][col] == '*':
                fr = row
                fc = col
            neighbours[(row, col)] = neighbour_counter(matrix, row, col, rows, cols)
    path = dfs(matrix, sr, sc, fr, fc, rows, cols)
    if neighbours[(sr, sc)] > 1:
      counter += 1
    for coordinates in path:
      if neighbours[coordinates] > 2 and coordinates != (sr, sc) and coordinates != (fr, fc):
        counter += 1
    if counter == k:
        return 'Impressed'
    else:
        return 'Oops!' 
def dfs(matrix, sr, sc, fr, fc, rows, cols):
    stack = Stack()
    stack.push([(sr, sc)])
    visited = set([(sr, sc)])
    while stack.size():
        path = stack.pop()
        row, col = path[-1]
        if row == fr and col == fc:
            return path
        for row2, col2 in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
            if 0 <= row2 < rows and 0 <= col2 < cols and matrix[row2][col2] != 'X' and (row2, col2) not in visited:
                stack.push(path + [(row2, col2)])
                visited.add((row2, col2))
def neighbour_counter(matrix, row, col, rows, cols):
  counter = 0
  if row > 0 and matrix[row - 1][col] != 'X':
    counter += 1
  if row < rows - 1 and matrix[row + 1][col] != 'X':
    counter += 1
  if col > 0 and matrix[row][col - 1] != 'X':
    counter += 1
  if col < cols - 1 and matrix[row][col + 1] != 'X':
    counter += 1
  return counter
https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem?isFullScreen=true
HackerRankHackerRank
Connected Cells in a Grid | HackerRank
Find the largest connected region in a 2D Matrix.
:fire:
1

9:06
# class Queue
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        return self.queue.append(value)
    def dequeue(self):
        if self.size():
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
# Complete the connectedCell function below.
def connectedCell(matrix):
    # var rows
    rows = len(matrix)
    # var cols
    cols = len(matrix[0])
    # var biggest_island
    biggest_island = 0
    print(matrix)
    # loop through the matrix
    for row in range(rows): 
        for col in range(cols):
            # if we reach a one
            if matrix[row][col] == 1:
                # call bfs => updating matrix, biggest island
                matrix, biggest_island = island_counter(matrix, row, col, rows, cols, biggest_island)
    # return biggest island
    return biggest_island
# island counter helper function
def island_counter(matrix, row1, col1, rows, cols, biggest_island):
     # var size_island
     size_island = 1
     matrix[row1][col1] = 0
     queue = Queue()
     queue.enqueue((row1, col1))
     # bfs
     while queue.size():
        row, col = queue.dequeue()
        for row2, col2 in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1), (row + 1, col + 1), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1)):
            if 0 <= row2 < rows and 0 <= col2 < cols and matrix[row2][col2] == 1:
                # update matrix that the founded island gets deleted
                size_island += 1
                matrix[row2][col2] = 0
                queue.enqueue((row2, col2))
     # if statement, check if size_island is bigger than biggest island
     if size_island > biggest_island:
        biggest_island = size_island
     #return matrix and size_island
     return matrix, biggest_island