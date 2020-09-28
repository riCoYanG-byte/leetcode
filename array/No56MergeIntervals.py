# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merge = []
        intervals.sort(key = lambda x:x[0])
        for inter in  intervals:
            if  not merge or  inter[0] > merge[-1][1]:
                merge.append(inter)
            else:
                merge[-1][1] =  max(inter[1],merge[-1][1])
        return merge