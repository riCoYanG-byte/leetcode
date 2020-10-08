# Definition for a binary tree node.
# a very concise way

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def longestConsecutive(self, root: TreeNode) -> int:
        def helper(node, prev, curr):
            if node is None:
                return curr

            elif prev is not None and node.val == prev.val + 1:
                return max(helper(node.left, node, curr + 1), helper(node.right, node, curr + 1))

            else:
                return max(curr, helper(node.left, node, 1), helper(node.right, node, 1))

        if not root:
            return 0
        return helper(root, None, 1)






