# Given
# a
# binary
# tree, collect
# a
# tree
# 's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
#
# Example:
#
# Input: [1, 2, 3, 4, 5]
#
# 1
# / \
#     2
# 3
# / \
#     4
# 5
#
# Output: [[4, 5, 3], [2], [1]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


def findLeaves(self, root):
    result = []
    while root is not None:
        leaves = []
        dfsTraverse(root,leaves)
        result.append(result)
    return leaves

def dfsTraverse(node, leaves):
    if not node:
        return
    if node.left is None and node.right is None:
        leaves.append(node.val)
        node = None
    dfsTraverse(node.left,leaves)
    dfsTraverse(node.right,leaves)


# 从下往上看是一个样子的

# class Solution:
#     def findLeaves(self, root):
#         res = collections.defaultdict(list)
#         def dfs(node):
#             if not node:
#                 return 0
#             left = dfs(node.left)
#             right = dfs(node.right)
#             height = max(left,right)+1
#             res[height].append(node.val)
#             return height
#         dfs(root)
#         return res.values()