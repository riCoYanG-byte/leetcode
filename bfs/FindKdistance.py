# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
#

# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        res = []
        while queue:

            node, d = queue.popleft()
            if d == K:
                res.append(node.val)
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return res

