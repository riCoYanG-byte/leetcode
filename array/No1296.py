import collections


# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets
# of k consecutive numbers Return True if its possible otherwise return False.

# 当前的最小的肯定配后面的都减掉
def isPossibleDivide(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    s = collections.Counter(nums)
    order_num = sorted(s)

    for num in order_num:
        cur = s[num]
        if cur > 0:
            for i in range(num + 1, num + k):
                if s[i] >= cur:
                    s[i] = s[i] - cur
                else:
                    return False
    return True
