def insertNodeAtPosition(llist, data, position):
    # Write your code here
    retList = SinglyLinkedList()
    retList.head = llist
    iterationNode = retList.head
    newNode = SinglyLinkedListNode(data)
    loc = 0
    if llist is None:
        retList.head = newNode
    elif position == 0:
        newNode.next = retList.head
        retList.head = newNode
    else:
        while(iterationNode is not None):
            if(position-1 == loc):
                newNode.next = iterationNode.next
                iterationNode.next = newNode
            loc += 1
            iterationNode = iterationNode.next
    return retList.head
            
