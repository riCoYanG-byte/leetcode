def longestPeak(array):
    # Write your code here.
    # find a peak
    peakList = []
    length = 0
    for i in range(len(array)):
        if i == 0:
            continue
        if i == len(array) - 1:
            break
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peakList.append(i)

    for i in range(len(peakList)):
        if getLength(peakList[i], array) > length:
            length = getLength(peakList[i], array)

    return length


def getLength(peaksIndex, array):
    left = peaksIndex
    right = peaksIndex
    while left >= 0:
        if array[left] > array[left - 1]:
            left = left - 1
        else:
            break

    while right < len(array)-1:
        if array[right] > array[right + 1]:
            right = right + 1
        else:
            break
    peaksLength = right - left + 1
    return peaksLength


print(longestPeak([1, 2, 3, 4, 5, 1]))
