# Given a non-empty array of integers, return the k most frequent elements.

# solution: 构建一个frequent小顶堆进行比较，如果下一个比堆顶小那么比较下一个，若比堆顶大则弹出下一个

# 直接构建一个小顶堆返回nlargest就完事了
import heapq
from collections import Counter

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == len(nums):
        return nums

    # 1. build hash map : character and how often it appears
    # O(N) time
    count = Counter(nums)
    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)
