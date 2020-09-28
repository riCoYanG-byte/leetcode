def spiralTraverse(array):
    # resultList
    result = []
    # Write your code here.
    # initialize
    startrows = 0
    endrows = len(array)
    startcols = 0
    endcols = len(array[0])

    while startrows < endrows and startcols < endcols:
        for col in range(startcols, endcols):
            result.append(array[startrows][col])
        for row in range(startrows + 1, endrows):
            result.append(array[row][endcols - 1])

        for col in reversed(range(startcols, endcols - 1)):
            if startrows == endrows - 1:
                break
            result.append(array[endrows - 1][col])
        for row in reversed(range(startrows + 1, endrows - 1)):
            if startcols == endcols - 1:
                break
            result.append(array[row][startcols])

        startrows = startrows + 1
        endrows = endrows - 1
        startcols = startcols + 1
        endcols = endcols - 1

    return result


print(spiralTraverse([[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]))
