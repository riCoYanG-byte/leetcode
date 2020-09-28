# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
#
# Note:
# A subtree must include all of its descendants.
#
# Example:
#
# Input: [10,5,15,1,8,null,7]
#
#    10
#    / \
#   5  15
#  / \   \
# 1   8   7
#
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []

        def helper(node):
            if node is None:
                return 0,0,float('inf'),float('-inf')

            Nleft,leftnum,minleft,maxleft = helper(root.left)
            Nright,rightnum,minright,maxright = helper(root.right) #右边的左子树里最小值

            if  maxleft < node.val < minright:
                N = leftnum + rightnum + 1
            else:
                N = float('-inf')
            return max(Nleft,Nright,N), N, min(minleft,node.val),max(maxright,node.val)

        return helper(root)[0]

