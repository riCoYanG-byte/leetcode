# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# each time only compare once to promise the correct order for the result
def mergeLinkedLists(headOne, headTwo):
    currentNode1 = headOne
    currentNode2 = headTwo
    prev = None
    while currentNode1 is not None and currentNode2 is not None:
        if currentNode1.value < currentNode2.value:
            prev = currentNode1
            currentNode1 = currentNode1.next
        else:
            if prev is not None:
                prev.next = currentNode2
            prev = currentNode2
            currentNode2 = currentNode2.next
            prev.next = currentNode1

    if currentNode1 is None:
        prev.next = currentNode2
    return headOne if headOne.value < headTwo.value else headTwo
