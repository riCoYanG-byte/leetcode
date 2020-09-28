# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []

        while root or stack:

            while root:
                # 如果右边有直接退回上一节点
                stack.append(root)
                root = root.left

            # 如果左子树和右子树都有就直接退回就行
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []

        while root:
            res.append(root.val)
            stack.append(root)

            if root.right:
                # 把左节点全遍历完了就可以了
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return res
