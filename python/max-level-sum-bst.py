#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (71.41%)
# Likes:    314
# Dislikes: 18
# Total Accepted:    34.3K
# Total Submissions: 47.6K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level X such that the sum of all the values of nodes at
# level X is maximal.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree is between 1 and 10^4.
# -10^5 <= node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        class Stack():
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
        s = Stack()
        visited = {}
        level_count = 0
        s.push([root])
        max_sum = 0
        max_level = 0
        while s.size() > 0:
            level_count += 1
            current_level = s.pop()
            path = list()
            for i in range(0, len(current_level)):
                if level_count not in visited:
                    visited[level_count] = current_level[i].val
                else:
                    visited[level_count] += current_level[i].val
                if current_level[i].left:
                    path.append(current_level[i].left)
                if current_level[i].right:
                    path.append(current_level[i].right)
            if len(path) > 0:
                s.push(path)
        for k in visited:
            if visited[k] > max_sum:
                max_sum = visited[k]
                max_level =  k
        return max_level
