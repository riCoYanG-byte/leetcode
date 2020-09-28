# complexity:O(n2)
# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count = 0
#         for min in range(len(nums)):
#             currentSum = 0
#             for max in range(min, len(nums)):
#                 currentSum += nums[max]
#                 if currentSum == k:
#                     count += 1
#         return count
#
#

# complexity:O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pj_dict = {0: 1}
        result, cur = 0, 0
        for num in nums:
            cur += num
            if cur - k in pj_dict:
                result += pj_dict[cur - k]
            if cur in pj_dict:
                pj_dict[cur] += 1
            else:
                pj_dict[cur] = 1

        return result
