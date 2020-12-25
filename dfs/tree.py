# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)

    def depth(self,node):
        if node.isleave(node):
            self.diameter += 1
        if node.left:
            self.depth(node.left)
        if node.right:
            self.depth(node.right)

    def isleave(self,node):
        if node.left is None and node.right is None:
            return True
        return False






