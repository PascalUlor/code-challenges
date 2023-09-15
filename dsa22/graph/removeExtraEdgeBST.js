/**Q) You are given a binary tree of N nodes. 
 * While it is mostly a valid binary tree, there is at most one extra edge that violates the binary tree property of having exactly one path from the root to any node. 
 * Your job is to design an algorithm to find that extra edge and eliminate it.
 */

class BTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function removeExtraEdge(root) {
    const stack = [];
    const visitedNodes = new Set();

    stack.push(root);
    visitedNodes.add(root);
    while (stack.length) {
        const node = stack.pop();
        if (node.left && visitedNodes.has(node.left)) {
            node.left = null;
            return root;
        }
        if (node.right && visitedNodes.has(node.right)) {
            node.right = null;
            return root;
        }

        if (node.left) {
            stack.push(node.left);
            visitedNodes.add(node.left);
        }
        if (node.right) {
            stack.push(node.right);
            visitedNodes.add(node.right);
        }
    }
    return root;
}

let A = new BTree('a');
let B = new BTree('b');
let C = new BTree('c');

A.left = B;
A.right = C;
C.left = B;

console.log(removeExtraEdge(A));

