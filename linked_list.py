# Create Node constructror
class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None #address to next node
    def __str__(self):
        return f"{self.data} → {self.next_node}"

# node = ListNode(5)
# node.next_node = 2

# print(node)

# create List Constructor that takes a value
class Linked_List(object):
#     # set node as None
#     # set head for linked list and 
#     # set a temp/tail variable to track address of linked lists
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_size = 0
    def __str__(self):
        return f"Head→{self.head}"

    def insert_node(self, data): #add a new node to linked list
        self.list_size += 1 #increment list size
        new_node = ListNode(data) # initialize new node
        if self.head is None:
            # at start of linked list the head is also the tail
            self.head = new_node
            self.tail = self.head
        else:
            # if linked list already exists
            self.tail.next_node = new_node # tail will hold address to new node
            self.tail = new_node # newly added node becomes new tail

    def get_size(self): # optimal approach with (O)1
        return self.list_size
    
    def get_size_traver(self): # (O)n works if we did not have size increment on inserting node
        actual_node = self.head
        size = 0
        while actual_node is not None:
            size += 1
            actual_node = actual_node.next_node
        return size
    
    def insert_at_start(self, data):
        self.list_size += 1 # increment size of array
        new_node = ListNode(data)
        if self.head is None: #if there is no head it means linked list is empty
            self.head = new_node # set head to new node if linked list is empty
        else:
            #if linked list is not empty set the address ref of new node to head
            new_node.next_node = self.head
            # now make the new node the head
            self.head = new_node

    def remove_node(self, data):
        # base case to ensure list in not empty
        if self.head is None:
            return
        # decrement size of list
        self.list_size -= 1
        # set head node to a variable
        current_node = self.head
        prev_node = None # since head node has no previous

        # traverse list
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next_node
        # if specified node to be deleted is the head then it wont have a previous
        if prev_node is None:
            self.head = current_node.next_node
        else:
            prev_node.next_node = current_node.next_node
    
    def traverse_node(self):
        actual_node = self.head

        # traverse list
        while actual_node is not None:
            print(f"{actual_node.data}")
            actual_node = actual_node.next_node
    
    def insert_at_end(self, data):
        self.list_size += 1
        new_node = ListNode(data)
        actual_node = self.tail

        # traverse to find the last node
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node
        actual_node.next_node = new_node

    def insert_at_pos(self, pos, data):
        if pos > self.list_size:
            print('invalid position')
        else:
            new_node = ListNode(data)
            current_node = self.head
            i = 0
            while i < pos:
                current_node = current_node.next_node
                i += 1
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

list_node = Linked_List()
list_node.insert_node(23)
list_node.insert_node(3)
list_node.insert_node(1)
list_node.insert_at_start(0)
# list_node.remove_node(0)
list_node.insert_at_end(100)
list_node.insert_at_pos(0, 4)
list_node.traverse_node()

print(list_node)
