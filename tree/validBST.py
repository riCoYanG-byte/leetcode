# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    max = float("inf")
    min = float("-inf")
    return isValid(tree, max, min)


def isValid(tree, max, min):
    if tree is None:
        return True
    if tree.value > max or tree.value < min:
        return False
    else:
        leftisV = isValid(tree.left, tree.value, min)
        rightisV = isValid(tree.right, max, tree.value)
        return leftisV and rightisV
