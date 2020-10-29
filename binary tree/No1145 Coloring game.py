# Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.
#
# Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.
#
# Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)
#
# If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
#
# You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        # get info
        firstNode = self.findNodes(root,x)
        left_branch = self.count_nodes(firstNode.left)
        right_branch = self.count_nodes(firstNode.right)
        remains = n - left_branch - right_branch

        # condition
        if left_branch + right_branch < remains \
                or left_branch + remains < right_branch \
                or right_branch + remains < left_branch:
            return True
        else:
            return False

    # get nodes number
    def count_nodes(self,node,total = 0):

        if not node:
            return
        total += 1
        self.count_nodes(node.left)
        self.count_nodes(node.right)

        return total

    # get target nodes
    def findNodes(self,node,target):
        if not node:
            return
        if node.val == target:
            return node
        self.findNodes(node.left)
        self.findNodes(node.right)
