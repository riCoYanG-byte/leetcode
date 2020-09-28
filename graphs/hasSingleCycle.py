def hasSingleCycle(array):
    # Write your code here.
    numbervisited = 0
    currentidx = 0
    while numbervisited < len(array):
        if numbervisited > 0 and currentidx == 0:
            return False
        currentidx = getNextidx(array, currentidx)
        numbervisited = numbervisited + 1
    return currentidx == 0


def getNextidx(array, currentidx):
    jump = array[currentidx]
    nextidx = (jump + currentidx) % len(array)
    if nextidx >= 0:
        return nextidx
    else:
        return nextidx + len(array)



