# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

import collections
import heapq


class Solution(object):
    def __init__(self):
        self.stack = []

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # vec graph
        vec = collections.defaultdict(list)
        for tic in tickets:
            fr = tic[0]
            ds = tic[1]
            vec[fr].append(ds)

        # use heap to sort
        for fr in vec:
            heapq.heapify(vec[fr])
        self.dfs(vec, 'JFK')
        return self.stack[::-1]

    # dfs not totally back traverse
    def dfs(self, vec, cur):
        while vec[cur]:
            temp = heapq.heappop(vec[cur])
            self.dfs(vec, temp)
        self.stack.append(cur)





