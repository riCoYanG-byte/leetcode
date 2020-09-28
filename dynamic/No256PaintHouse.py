# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
#

# Algorithm1 using the tree to represent the chioce of painting houses

# time limited: down ---> up use recursions
class Solution(object):
    def minCost(self, costs):

        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:  # Red
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:  # Green
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:  # Blue
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))

# use a cache to remember the middle result

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        def paint_cost(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost

        if costs == []:
            return 0

        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))