from idlelib.tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        result = self.dfs(root, sum)
        return result

    def dfs(self, node, remain_sum):
        if not node:
            return
        if remain_sum == node.val and not node.left and not node.right:
            return True
        # 相当于把下层信息传递到上层
        return self.dfs(node.left, remain_sum - node.val) or self.dfs(node.right, remain_sum - node.val)


