# Python3 implementation of the approach
"""
Take two pointers, first will point to the head of the linked list and second will point to the Nth node from the beginning.
Now keep increment both the pointers by one at the same time until second is pointing to the last node of the linked list.
After the operations from the previous step, first pointer should be pointing to the Nth node from the end by now. So, delete the node first pointer is pointing to.
"""


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):

            # If count of nodes in the
            # given list is less than 'n'
            if(second.next == None):

                # If index = n then
                # delete the head node
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next

        while(second.next != None):
            second = second.next
            first = first.next

        first.next = first.next.next

    def printList(self):
        tmp_head = self.head
        while(tmp_head != None):
            print(tmp_head.data, end=' ')
            tmp_head = tmp_head.next


# Driver Code
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
print("Created Linked list is:")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion is:")
llist.printList()

# This code is contributed by RaviParkash
