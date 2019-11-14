from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # pass
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        # pass
        # remove item from stack
        if self.size > 0 and self.size != 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None


    def len(self):
        # pass
        # get number of items in stack
        if self.size > 0:
            return self.size
        else:
            return 0
