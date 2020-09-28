# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
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
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True

        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while currentNode is not None:
            if currentNode.value < self.value:
                parrentNode = currentNode
                currentNode = currentNode.right
            elif currentNode > self.value:
                parrentNode = currentNode
                currentNode = currentNode.left
            else:
                # first situation : left and right both none
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinVal()
                    currentNode.right.remove(currentNode, currentNode.value)
                elif parrentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.left
                        currentNode.left = currentNode.right.right
                    else:
                        currentNode.value = None
                elif currentNode == parrentNode.left:
                    parrentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif currentNode == parrentNode.right:
                    parrentNode.right == currentNode.left if currentNode.left is not None else currentNode.right
                break

        return self

    def getMinVal(self):
        currentNode = self
        while currentNode.left is not None:
            break
        return self
