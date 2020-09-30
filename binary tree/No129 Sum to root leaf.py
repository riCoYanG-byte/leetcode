# non recursive
# 可以通过堆栈进行dfs
from idlelib.tree import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode):
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    # 始终把current num存起来
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf