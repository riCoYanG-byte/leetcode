# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    counter = 1
    first = head
    second = head
    while counter < k + 1:
        first = first.next
        counter = counter + 1
        if first is None:
            head.value = head.next.value
            head.next = head.next.next
            return
        prev = second
    while first is not None:
        prev = second
        second = second.next
        first = first.next
        if second.next is None:
            print(1)
            prev.next = None
        else:
            prev.next = prev.next.next
