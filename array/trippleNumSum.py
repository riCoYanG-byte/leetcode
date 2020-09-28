def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            ourTarget = array[left] + array[i] + array[right]
            if ourTarget == targetSum:
                result.append([array[i], array[left], array[right]])
                left = left + 1
                right = right - 1
            elif ourTarget < targetSum:
                left = left + 1
            elif ourTarget > targetSum:
                right = right - 1
    return result


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
