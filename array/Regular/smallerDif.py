def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    # Write your code here
    smallestPair = []
    smallest = float("inf")
    current = float("inf")
    # at first sort the two array
    # arrayOne.sort()
    # arrayTwo.sort()
    # pointer
    point1 = 0
    point2 = 0
    # reverse
    while point1 < len(arrayOne) and point2 < len(arrayTwo):
        # sum = abs(arrayOne[point1]-arrayTwo[point2])
        firstNum = arrayOne[point1]
        SecondNum = arrayTwo[point2]
        if firstNum < SecondNum:
            current = SecondNum - firstNum
            point1 = point1 + 1
        elif firstNum > SecondNum:
            current = firstNum - SecondNum
            point2 = point2 + 1
        else:
            return [firstNum, SecondNum]
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, SecondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
