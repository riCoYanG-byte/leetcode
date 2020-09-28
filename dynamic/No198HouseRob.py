# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, array):
        # Write your code here.
        if len(array) == 0:
            return 0
        elif len(array) == 1:
            return array[0]
        else:
            maxSum = array[:]
            maxSum[0] = array[0]
            maxSum[1] = array[0] if array[0] > array[1] else array[1]
            for i in range(2, len(array)):
                # 反正就不可能包含array[i]
                maxSum[i] = maxSum[i - 1] if maxSum[i - 1] > maxSum[i - 2] + array[i] else maxSum[i - 2] + array[i]
            return maxSum[len(array) - 1]

