# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2



import collections
class Solution(object):
    def __init__(self):
        self.visited = []
        self.vec = collections.defaultdict(list)

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.visited = [False] * n
        for v1,v2 in edges:
            self.vec[v1].append(v2)
            self.vec[v2].append(v1)

        component = 0
        for node in range(n):
            if self.visited[node] is False:
                print(self.visited)
                component += 1
                self.dfs(node)
            else:
                continue
        return component

    def dfs(self,node):
        self.visited[node] = True
        for nei in self.vec[node]:
            if self.visited[nei] is False:
                self.dfs(nei)
            else:
                continue



