def minHeightBst(array):
    return consTruct(array, None, 0, len(array) - 1)


def consTruct(array, tree, start, end):
    if start > end:
        return
    middle = (start + end) // 2
    addV = array[middle]
    if tree is None:
        tree = BST(addV)
    else:
        tree.insert(addV)
    consTruct(array, tree, start, middle - 1)
    consTruct(array, tree, middle + 1, end)
    return tree


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
