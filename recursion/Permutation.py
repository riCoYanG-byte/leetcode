def getPermutations(array):
    # Write your code here.
    permutation = []
    permutationHelper(array, [], permutation)
    return permutation


def permutationHelper(array, currentPer, permutation):
    if len(array) == 0:
        permutation.append(currentPer)
    else:
        for num in range(len(array)):
            newArr = array[:num] + array[num + 1:]
            newPer = currentPer + [array[num]]
            permutationHelper(newArr, newPer, permutation)


print(getPermutations([1, 2, 3]))
