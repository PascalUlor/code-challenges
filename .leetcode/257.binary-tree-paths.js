/*
 * @lc app=leetcode id=257 lang=javascript
 *
 * [257] Binary Tree Paths
 *
 * https://leetcode.com/problems/binary-tree-paths/description/
 *
 * algorithms
 * Easy (59.34%)
 * Likes:    5452
 * Dislikes: 236
 * Total Accepted:    597.5K
 * Total Submissions: 976.8K
 * Testcase Example:  '[1,2,3,null,5]'
 *
 * Given the root of a binary tree, return all root-to-leaf paths in any
 * order.
 * 
 * A leaf is a node with no children.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [1,2,3,null,5]
 * Output: ["1->2->5","1->3"]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1]
 * Output: ["1"]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [1, 100].
 * -100 <= Node.val <= 100
 * 
 * 
 */

// @lc code=start
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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    let path = [];
    dfsTraversal(root, path, "");
    return path;
};
const dfsTraversal = (root, path, traversalMap) => {
    if(!root) {
        return []
    }
    if(!root.left && !root.right) {
        path.push(traversalMap + root.val)
        return;
    }
    if(root.left) {
        dfsTraversal(root.left, path, traversalMap + root.val + "->")
    }

    if(root.right) {
        dfsTraversal(root.right, path, traversalMap + root.val + "->")
    }
}
// @lc code=end

