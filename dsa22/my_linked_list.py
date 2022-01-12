class ListNode(object):
    def __init__(self, value=None):
        self.val = value
        self.next = None 

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.list_size = 0
        

    def get(self, index: int) -> int:
        if index >= self.list_size or index < 0:
            return -1
        elif self.head is None:
            return -1
        else:
            i = 0
            current_node = self.head
            while i < index:
                current_node = current_node.next
                i += 1
            return current_node.val
        

    def addAtHead(self, val: int) -> None:
        self.list_size += 1
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            prev_head = self.head
            self.head = new_node
            self.head.next = prev_head
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
        else:
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node
            
        self.list_size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if index > self.list_size:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            i = 0
            curr_node = self.head
            while i < index-1:
                curr_node = curr_node.next
                i += 1
            new_node.next = curr_node.next
            curr_node.next = new_node
            self.list_size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        curr_node = self.head
        if index >= self.list_size or index < 0:
            return
        elif index == 0:
            self.head = curr_node.next
        else:
            i = 0
            while i < index-1:
                curr_node = curr_node.next
                i += 1
            curr_node.next = curr_node.next.next
        self.list_size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)