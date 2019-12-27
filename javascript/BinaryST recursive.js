/** Constructor
 * value
 * left
 * right
 *
 * ==Methods==
 * insert(value) goal: find itsnpropermplace
 * if value < current
 *      if(left) go left
 *      else insert
 *  if value > current
 *      if(right) go right
 *      else insert
 *
 * ==Contains==
 * **/

class BinarySearchTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BinarySearchTree(value);
      }
      this.left.insert(value);
    }
    if (value > this.value) {
      if (this.right === null) {
        this.right = new BinarySearchTree(value);
      }
      this.right.insert(value);
    }
    return this;
  }
  contains(value) {
    if (this.value === value) return true;
    if (value < this.value) {
      return !!this.left && this.left.contains(value);
    }
    if (value > this.value) {
      return !!this.right && this.right.contains(value);
    }
    return false;
  }

  inOrder(node){
    if(node.left){
      this.inOrder(node.left)
    }
    console.log(node.value)
    if(node.right){
      this.inOrder(node.right)
    }
  }
  preOrder(node){
    console.log(node.value)
    if(node.left){
      this.preOrder(node.left)
    }
    if(node.right){
      this.preOrder(node.right)
    }
  }
  postOrder(node){
    if(node.left){
      this.preOrder(node.left)
    }
    if(node.right){
      this.preOrder(node.right)
    }
    console.log(node.value)
  }
}

const tree = new BinarySearchTree(11);
tree.insert(10);
tree.insert(5);
tree.insert(13);
tree.insert(11);
tree.insert(2);
tree.insert(16);
tree.insert(7);
tree.contains(10);

const tree = new BinarySearchTree(11);
tree
  .insert(10)
  .insert(5)
  .insert(13)
  .insert(11)
  .insert(2)
  .insert(16)
  .insert(7);
