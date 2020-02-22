// Complete the insertNodeAtPosition function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtPosition(head, data, position) {
    let count = 0;
    if (position === 0 && !head) {
        head.data = data;
    };
    let currentNode = head;
    let newNode = new SinglyLinkedListNode(data);
    while (count < position-1) {
        currentNode = currentNode.next;
        count += 1;
    }
    newNode.next = currentNode.next;
    currentNode.next = newNode;
    return head;
    };