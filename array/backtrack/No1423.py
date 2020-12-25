# 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
#
# 每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
#
# 你的点数就是你拿到手中的所有卡牌的点数之和。
#
# 给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
#
#
# dfs会超时

def dfs(cardPoints, k):
    left = 0
    right = len(cardPoints) - 1
    if k == 1:
        return max(cardPoints[left], cardPoints[right])
    else:
        lmax = dfs(cardPoints[1:], k - 1) + cardPoints[0]
        rmax = dfs(cardPoints[:len(cardPoints) - 1], k - 1) + cardPoints[len(cardPoints) - 1]
        return max(lmax, rmax)


def maxScore(cardPoints, k):
    if k == 0:
        return max(cardPoints[0], cardPoints[len(cardPoints) - 1])
    if k == len(cardPoints):
        return sum(cardPoints)

    return dfs(cardPoints, k)


# 此时不如使用互动窗口来做
# [1:2] 切片左闭右开
# 一般不要用sum来做会超时
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) == k:  # 如果取的次数等于长度，说明把所有牌都取走，直接返回总和
            return sum(cardPoints)

        left  = 0
        right = len(cardPoints)-k-1
        currentSum = sum(cardPoints[:right+1])
        for _ in range(k):
            left += 1
            right += 1
            temp = sum(cardPoints[left:right+1])
            currentSum = min(currentSum,temp)
        return sum(cardPoints)-currentSum
