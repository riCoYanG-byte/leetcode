# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,

#   5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1

from idlelib.tree import TreeNode

from astroid import List


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathList = []
        self.dfs(root, sum,[], pathList)
        return pathList

    def dfs(self,node,remain_sum,pathNodes,pathList):
        if not node:
            return
        pathNodes.append(node.val)
        if remain_sum == node.val and not node.left and not node.right:
            pathList.append(list(pathNodes))
        else:
            self.dfs(node.left,remain_sum-node.val,pathNodes,pathList)
            self.dfs(node.right,remain_sum-node.val,pathNodes,pathList)

        pathNodes.pop()



