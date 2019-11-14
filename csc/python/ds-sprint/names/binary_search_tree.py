import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value #root
        self.left = None
        self.right = None
        self.stack = Stack()
        self.queue = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        if  self.value == target:
            return True
        
        if self.left is None and self.right is None:
            return False
        
        if target < self.value and self.left is not None:
            return self.left.contains(target)
        elif self.right is not None:
            return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        if self.value is None:
            return None
        
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # pass
        if self.value is None:
            return None
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # pass
        current_node = node
        print(current_node.value)
        if current_node.right is not None:
            self.stack.push(current_node.right)
        elif current_node.left is not None:
            self.stack.push(current_node.left)
        
        if not self.stack.len():
            return
        self.in_order_print(self.stack.pop())

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        # use a queue data structure
        current_node = node
        # enqueue the starting node on to the queue
        self.queue.enqueue(current_node)
        # loop while the queue has data
        while self.queue.len() > 0:
            # dequeue the current it em off the queue
            self.queue.dequeue()
            # print the current value
            print(current_node)
            # if the current node has a left child
            if current_node.left:
                # enqueue the left child on to the queue
                self.queue.enqueue(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # enqueue right child on to the queue
                self.queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass
        # pass
        # use a queue data structure
        current_node = node
        # enqueue the starting node on to the queue
        self.stack.push(current_node)
        # loop while the queue has data
        while self.stack.len() > 0:
            # dequeue the current it em off the queue
            self.stack.pop()
            # print the current value
            print(current_node)
            # if the current node has a left child
            if current_node.left:
                # enqueue the left child on to the queue
                self.stack.push(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # enqueue right child on to the queue
                self.stack.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
