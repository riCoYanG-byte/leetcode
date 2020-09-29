def reverseLinkedList(head):
    # Write your code here.
    left, mid, right = None, head, None
    while mid is not None:
        right = mid.next
        mid.next = left
        left = mid
        mid = right
        # non null version

    return left
