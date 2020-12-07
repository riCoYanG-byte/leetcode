# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
#
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
#
# Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b

# easy to finish
def findMissingRanges(self, A, lower, upper):
    result = []
    A.append(upper + 1)
    # 把开头计算上，分两种情况去讨论1.隔一个 2.隔一个有序序列
    pre = lower - 1
    for i in A:
        if (i == pre + 2):
            result.append(str(i - 1))
        elif (i > pre + 2):
            result.append(str(pre + 1) + "->" + str(i - 1))
        pre = i
    return result