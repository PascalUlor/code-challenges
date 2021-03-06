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
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        # pass
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        # pass
        return self.size
