import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # pass
        # add item to queue
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # pass
        # remove item from queue
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        # pass
        # number of items in queue
        if self.size > 0:
            return self.size
        else:
            return 0
