# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isLeaves(self,node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    #add leaves
    # by using dfs we can make sure the leaves
    def addLeaves(self,node,res):
        if self.isLeaves(node):
            res.append(node)
        else:
            if node.left:
                self.addLeaves(node,res)
            else:
                self.addLeaves(node,res)

    # divide it into three parts
    def boundaryOfBinaryTree(self, root):
        # dive into the  leftmost
        node = root
        res =  [node]

        node = root.left
        while node:
            if self.isLeaves(node):
                res.append(node)
            if node.left:
                node = node.left
            else:
                node = node.right

        # add leaves
        self.addLeaves(root,res)

        #get right most by using stack
        stack = []
        node = root.right
        while node:
            if self.isLeaves(node):
                stack.append(node)
            if node.right:
                node = node.right
            else:
                node = node.left

        #add stack
        while stack:
            res.append(stack.pop())

        return res


# 最简单的方法是前序遍历，然后判断是不是叶子节点
