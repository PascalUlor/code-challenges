"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # pass
        # make a new node
        new_node = ListNode(value, None, None)
        # grow the length of the linked list
        self.length += 1

        # if this is not head or tail (singular node)
        if not self.head and not self.tail:
            # set the head and tail to this new node
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new nodes to the current head
            new_node.next = self.head
            #set the prev to the new node
            self.head.prev = new_node
            # set the head ref to the new node
            self.head = new_node

    def remove_from_head(self):
        # pass
        # set the return value to the value of the head
        value = self.head.value
        #delete head
        self.delete(self.head)
        #return the value
        return value

    def add_to_tail(self, value):
        # pass
        # make a new node
        new_node = ListNode(value, None, None)
        # grow the length of the linked list
        self.length += 1

        # if this is not head or tail (singular node)
        if not self.head and not self.tail:
            # set the head and tail to this new node
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
             # set the new nodes Prev to the current tail
             new_node.prev = self.tail
             # set the tails next to the new node
             self.tail.next = new_node
             # set the tail ref to the new node
             self.tail = new_node

    def remove_from_tail(self):
        # pass
        # set the return value to the tail value
        value = self.tail.value
        # delete the tail
        self.delete(self.tail)
        # return the value
        return value

    def move_to_front(self, node):
        # pass
        # if node is the head then return
        if node is self.head:
            return
        # set value to nodes value
        value = node.value
        # if the node is the tail
        if node is self.tail:
            # remove node from tail
            self.remove_from_tail()
        # otherwise
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1

        # add the value to the head
        self.add_to_head(value)

    def move_to_end(self, node):
        # pass
        # if node is tail then return
        if node is self.tail:
            return
        # set value to nodes values
        value = node.value
        # if the node is the head
        if node is self.head:
            # remove node from head
            self.remove_from_head()
        # otherwise
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1

        # add the value to the tail
        self.add_to_tail(value)

    def delete(self, node):
        # pass
        # decrement the length
        self.length -= 1
        # if not head or tail return
        if not self.head and not self.tail:
            return
        # if the head is the tail
        if self.head == self.tail:
            #set the head and tail to none
            self.head = None
            self.tail = None
        # otherwise if head is the node
        elif self.head == node:
            # set the head to the nodes next
            self.head = node.next
            # delete node
            node.delete()
        # otherwise if tail is the node
        elif self.tail == node:
            # set the tail to the nodes prev
            self.tail = node.prev
            # delete node
            node.delete()
        # otherwise
        else:
            # delete node
            node.delete()

    def get_max(self):
        # pass
        # if no head the return None
        if not self.head:
            return None
        # set the initial max value to the heads value
        max_value = self.head.value
        # set current node to head
        current_node = self.head
        # loop over nodes while current exist
        while current_node:
            # if current value is greater than the max value
            if current_node.value > max_value:
                # set the max value to the current value
                max_value = current_node.value
            # move to the next node
            current_node = current_node.next
        # return max value
        return max_value

    def find(self, value):
        node = self.head
        if node.value == value:
            return node
        while self.tail is not node:
            node = node.next
            if node.value == value:
                    return node
        return None
