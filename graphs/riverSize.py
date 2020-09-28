def riverSizes(matrix):
    sizes = []
    checkVisted = [[False for values in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if checkVisted[i][j] is False:
                tranverseNode(i, j, matrix, checkVisted, sizes)
            else:
                continue

    return sizes


def getNodesTo(i, j, matrix, checkVisted, nodesToExplore):
    if i > 0 and checkVisted[i - 1][j] is False:
        nodesToExplore.append([i - 1, j])
    if i < len(matrix) - 1 and checkVisted[i + 1][j] is False:
        nodesToExplore.append([i + 1, j])
    if j > 0 and checkVisted[i][j - 1] is False:
        nodesToExplore.append([i, j - 1])
    if j < len(matrix[0]) - 1 and checkVisted[i][j + 1] is False:
        nodesToExplore.append([i, j + 1])


def tranverseNode(i, j, matrix, checkVisted, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if checkVisted[i][j] is True:
            continue
        checkVisted[i][j] = True
        if matrix[i][j] == 0:
            continue
        getNodesTo(i, j, matrix, checkVisted, nodesToExplore)
        currentRiverSize += 1

    if currentRiverSize != 0:
        sizes.append(currentRiverSize)


print(riverSizes([
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]))
