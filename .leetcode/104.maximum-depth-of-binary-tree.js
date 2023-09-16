/*
 * @lc app=leetcode id=104 lang=javascript
 *
 * [104] Maximum Depth of Binary Tree
 *
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (74.30%)
 * Likes:    11818
 * Dislikes: 192
 * Total Accepted:    2.6M
 * Total Submissions: 3.5M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return its maximum depth.
 * 
 * A binary tree's maximum depth is the number of nodes along the longest path
 * from the root node down to the farthest leaf node.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [3,9,20,null,null,15,7]
 * Output: 3
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1,null,2]
 * Output: 2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [0, 10^4].
 * -100 <= Node.val <= 100
 * 
 * 
 */

// @lc code=start
class Stack {
    constructor() {
        this.stack = [];
    }

    push(value) {
        return this.stack.push(value);
    }
    pop() {
        if(this.size()) {
           return this.stack.pop();
        }
        return null;
    }

    size() {
        return this.stack.length;
    }
}
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    let maxCount = 0;
    const stack = new Stack();

    stack.push([root, 1]);

    while(stack.size()) {
        const [node, depth] = stack.pop();
        if (node) {
            if (!node.left && !node.right) {
                maxCount = Math.max(maxCount, depth);
            } else {
                stack.push([node.left, depth + 1]);
                stack.push([node.right, depth + 1]);
            }
        } 
    }
    return maxCount;
};
// @lc code=end

