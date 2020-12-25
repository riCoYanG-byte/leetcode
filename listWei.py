class Solution(object):

    def depthSum(self, nestedList, depth=1):
        """
        :param depth:
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        sum = 0
        for ele in nestedList:
            if ele.isInteger() is True:
                sum += ele.getInteger() * depth
            else:
                sum += self.depthSum(ele.getList(), depth + 1)

        return sum