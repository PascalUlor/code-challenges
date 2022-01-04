#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (42.84%)
# Likes:    3824
# Dislikes: 184
# Total Accepted:    198.7K
# Total Submissions: 459.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 
# 
#

# @lc code=start
# setup a stack ds
class Stack:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.size() > 0:
            return self.storage.pop()
        else:
            return None
def dfs (mat, i, j, row_len, col_len):
    # setup counter to calc dist
    min_dist = 0
    # push cell to stack
    stack = Stack()
    stack.push([(i, j)])

    while (stack.size() > 0):
        node = stack.pop()
        row, col = node[-1]

        for row2, col2 in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if 0 <= row2 < row_len and 0 <= col2 < col_len:
                if (row2 > 0 and mat[row2 - 1][col2] == 0) or (row2 < row - 1 and mat[row2 + 1][col2] == 0) or (col2 > 0 and mat[row2][col2 - 1] == 0) or (col2 < col2 - 1 and mat[row2][col2 + 1] == 0):
                    if min_dist < 0:
                        min_dist += mat[row2][col2]
                        print((row2, col2), min_dist)

    return min_dist;

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #get rows and cols length
        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows):
            for j in range(cols):
                cell = mat[i][j]
                if cell == 1:
                    # calc dist to nearest zero
                    dist = dfs(mat, i, j, rows, cols)
                    # update cell dist
                    if dist > 0:
                        print(dist)
                        mat[i][j] = dist
                    
        return mat

        
# @lc code=end

