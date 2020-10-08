# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def countNodes(self, root: TreeNode) -> int:
        # dfs
        self.dfs(root)
        return self.count

    def dfs(self,node):
        if not node:
            return
        self.count += 1
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)

