# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# 通过判断有环无环来确定能否修完全部courses

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build the graph
        from collections import defaultdict
        course_dict = defaultdict(list)

        # build the adjacent graph
        for courseS in prerequisites:
            prev, nextC = courseS[0], courseS[1]
            course_dict[prev].append(nextC)

        path = [False] * numCourses
        for cur in range(numCourses):
            if self.isCycle(cur, course_dict, path):
                return False
        return True

    def isCycle(self, cur, course_dict, path):
        # dfs
        if path[cur] is True:
            return True
        path[cur] = True

        res = False
        for child in course_dict[cur]:
            res = self.isCycle(child, course_dict, path)
            if res: break
        path[cur] = False
        return res
