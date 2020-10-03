# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# 这个跟permutation是一样的（宝贝）
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.backTracking(target,[],0)
        self.result = []
        self.candidates = candidates
        # self.target = target
        return self.result

    def backTracking(self,remain,comp,start):
        if remain == 0:
            self.result.append(list(comp))
        if remain<0:
            return
        for i in range(len(self.candidates)):
            # 这题是因为在这里已经添加了
            comp.append(self.candidates[i])
            self.backTracking(remain-self.candidates[i],comp,i)
            comp.pop()


