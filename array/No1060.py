# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.
# 数值分析，找空位置
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # return count of numbers the dix omit
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing(n - 1):
            return k - missing(n - 1) + nums[n - 1]

        idx = 0
        while missing(idx) < k:
            idx += 1
        return k - missing(idx - 1) + nums[idx - 1]

