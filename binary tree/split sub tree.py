# Input: root = [4,2,6,1,3,5,7], V = 2
# Output: [[2,1],[4,3,6,null,null,5,7]]
# Explanation:
# Note that root, output[0], and output[1] are TreeNode objects, not arrays.
#
# The given tree [4,2,6,1,3,5,7] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7
#
# while the diagrams for the outputs are:
#
#           4
#         /   \
#       3      6      and    2
#             / \           /
#            5   7         1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        #  using recursion
        if not root:
            return None, None
        if root.val <= V:
            bns = self.splitBST(root.right,V)
            root.right = bns[0]
            # 如果这个节点 < 当前的值，那么他左边的root都比他小，右边的有可能比他小，还要在细分
            # 返回上层分的结果，将左边的连接 起来就行
            # 这一步做的是连接子树的操作

            return root, bns[1]
        else:
            bns = self.splitBST(root.left,V)
            # 所以这里做的就是子树，连接的操作
            root.left = bns[1]
            return bns[0], root
