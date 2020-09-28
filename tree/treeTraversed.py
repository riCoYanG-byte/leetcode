# pre in post
def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array
    else:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
        return array

    def preOrderTraverse(tree, array):
        # Write your code here.
        if tree is None:
            return array
        else:
            array.append(tree.value)
            preOrderTraverse(tree.left, array)
            preOrderTraverse(tree.right, array)
            return array

    def postOrderTraverse(tree, array):
        # Write your code here.
        if tree is None:
            return array
        else:
            postOrderTraverse(tree.left, array)
            postOrderTraverse(tree.right, array)
            array.append(tree.value)
            return array
