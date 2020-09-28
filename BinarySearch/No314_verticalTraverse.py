# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# idea: 利用bfs广度遍历保证了从上到下的层级顺序然后按照column去排列即可
import collections


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()

        queue.append((root,0))
        # queue.append((root,0)) 不行

        columnTable = collections.defaultdict(list)

        while queue:
            node,column = queue.popleft()
            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left,column-1))
                queue.append((node.right,column+1))

        result = [columnTable[node] for node in sorted(columnTable.keys())]
        return result






