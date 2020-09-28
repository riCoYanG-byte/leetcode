# 1 2 3 5 4 3 2 1 4 5
# Given two sequences pushed and popped with distinct values,
# return true if and only if this
# could have been the result of a sequence of push and pop operations on an initially empty stack.


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        popid = 0
        stack = []
        for ele in pushed:
            stack.append(ele)
            # 这里用while全部检测出来
            while stack and stack[-1] == popped[popid]:
                stack.pop()
                popid += 1
        return not stack

