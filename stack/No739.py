# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# When i = 7, stack = [7 (73)]. ans[i] = 0.
# When i = 6, stack = [6 (76)]. ans[i] = 0.
# When i = 5, stack = [5 (72), 6 (76)]. ans[i] = 1.
# When i = 4, stack = [4 (69), 5 (72), 6 (76)]. ans[i] = 1.
# When i = 3, stack = [3 (71), 5 (72), 6 (76)]. ans[i] = 2.
# When i = 2, stack = [2 (75), 6 (76)]. ans[i] = 4.
# When i = 1, stack = [1 (74), 2 (75), 6 (76)]. ans[i] = 1.
# When i = 0, stack = [0 (73), 1 (74), 2 (75), 6 (76)]. ans[i] = 1.


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i in reversed(range(len(T))):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans