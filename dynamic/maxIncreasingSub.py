def getSequence(array, sequence, curidx):
    res = []
    while curidx is not None:
        res.append(array[curidx])
        curidx = sequence[curidx]
    return list(reversed(res))


def maxSumIncreasingSubsequence(array):
    maxidx = 0
    sums = array[:]
    sequence = [None for seq in range(len(array))]
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if array[j] < array[i] and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequence[i] = j
    for i in range(len(array)):
        if array[i] >= array[maxidx]:
            maxidx = i

    return [max(sums), getSequence(array, sequence, maxidx)]


print(maxSumIncreasingSubsequence([1, 2, 5, 4]))
