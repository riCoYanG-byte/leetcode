def shiftLinkedList(head, k):
    # Write your code here.
    # get length
    currentLength = 1
    countList = head
    while countList.next is not None:
        countList = countList.next
        currentLength += 1

    # get offset
    # k = 2 listLength = 6 newPos = 4
    # k=-2 newPos  = 2

    offset = abs(k) % currentLength
    if offset == 0:
        return head

    newPosition = currentLength - offset if k > 0 else offset
    newTail = head
    for i in range(1, newPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    countList.next = head
    return newHead


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
