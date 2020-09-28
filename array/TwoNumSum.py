def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentNum = array[left] + array[right]
        if currentNum == targetSum:
            return [array[left], array[right]]
        elif currentNum < targetSum:
            left = left + 1
        elif currentNum > targetSum:
            right = right - 1

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
