class Solution(object):

    # 双指针更简单一些
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 不断移动比较小的值，反正都是要移动的，不如把最小的移动了，有可能获得更大的值
        leftidx = 0
        rightidx = len(height) - 1

        # min height 才能决定容器
        currentArea = (rightidx - leftidx) * min(height[rightidx], height[leftidx])
        while leftidx < rightidx:
            if height[leftidx] < height[rightidx]:
                leftidx += 1
            else:
                rightidx -= 1
            currentArea = max(currentArea, (rightidx - leftidx) * min(height[rightidx], height[leftidx]))

        return currentArea
