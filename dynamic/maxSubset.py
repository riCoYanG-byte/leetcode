def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        maxSum = array[:]
        maxSum[0] = array[0]
        maxSum[1] = array[0] if array[0] > array[1] else array[1]
        for i in range(2,len(array)):
            maxSum[i] = maxSum[i-1] if maxSum[i-1] > maxSum[i-2]+array[i] else maxSum[i-2]+array[i]
        return maxSum[len(array)-1]

