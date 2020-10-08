from idlelib.tree import TreeNode
from typing import List
# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#

# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            print(node.left)
            node.right = helper(node.right)

            # process it after reversing
            # add children of a node that is to be deleted
            if node.val in to_delete:
                if node.left:
                    # 这里可以append进来一整个树{相当于弄的节点}
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                    # 相当于边遍历边删除
                    # 在这里作删除的
                return None
            return node

        helper(root)
        # if root is not to be deleted then add it
        if root.val not in to_delete:
            ans.append(root)
        return ans