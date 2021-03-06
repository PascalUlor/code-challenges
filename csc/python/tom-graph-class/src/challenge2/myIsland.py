# island count problem
from util import Queue, Stack


def numIslands(grid):
    rowDimension = len(grid)
    colDimension = len(grid[0]) if grid[0] else len(grid)
    queue = Queue()
    visited = []
    count = 0
    for rowIndex in range(rowDimension):
        for colIndex in range(colDimension):
            if grid[rowIndex][colIndex] == "1":
                queue.enqueue([rowIndex, colIndex])
                while queue.size() > 0:
                    currentNode = queue.dequeue()
                    visited.append(grid[currentNode[0]][currentNode[1]])
                    rx = currentNode[0]
                    cy = currentNode[1]
                    if grid[rx][cy] == "1":
                        grid[rx][cy] = "-1"
                        if rx + 1 >= 0 and rx + 1 < rowDimension and cy >= 0 and cy < colDimension:
                            queue.enqueue([rx + 1, cy])
                        if rx - 1 >= 0 and rx - 1 < rowDimension and cy >= 0 and cy < colDimension:
                            queue.enqueue([rx - 1, cy])
                        if rx >= 0 and rx < rowDimension and cy + 1 >= 0 and cy + 1 < colDimension:
                            queue.enqueue([rx, cy + 1])
                        if rx >= 0 and rx < rowDimension and cy - 1 >= 0 and cy - 1 < colDimension:
                            queue.enqueue([rx, cy - 1])
                count += 1

    return count


print(
    numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])
)

print(
    numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])
)

print(numIslands([["1", "0", "1", "1", "0", "1", "1"]]))
