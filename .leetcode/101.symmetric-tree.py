#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (49.62%)
# Likes:    8161
# Dislikes: 201
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,null,3,null,3]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# create a queue
class Queue:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)
    
    def enqueue(self, value):
        self.storage.append(value)
    
    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # check if root is null
        # if root is null return False
        if root is None:
            return False

        # check if root is a single node
        # if root is a single node then return true
        if root.left is None and root.right is None:
            return True

        #setup a queue to traverse the tree
        q = Queue()

        # enqueue the root for left and right traversal
        # left_tree
        q.enqueue(root)

        # right_tree
        q.enqueue(root)

        # setup variable to track each node
        left_node = 0
        right_node = 0

        #traverse the tree and compare the left and right nodes traversal
        while (q.size() > 0):
            left_node = q.dequeue()
            right_node = q.dequeue()

            # compare left_node and right_node
            if (left_node.val != right_node.val) or (left_node.val != right_node.val):
                return False

            if (left_node.left and right_node.right):
                q.enqueue(left_node.left)
                q.enqueue(right_node.right)
            elif (left_node.left or right_node.right):
                return False

            if (left_node.right and right_node.left):
                q.enqueue(left_node.right)
                q.enqueue(right_node.left)
            elif (left_node.right or right_node.left):
                return False

        return True
        
# @lc code=end

