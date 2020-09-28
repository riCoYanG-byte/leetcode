def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True


    if arrayOne[0] != arrayTwo[0]:
        return False

    if len(arrayOne) != len(arrayTwo):
        return False

    else:
        left1 = getSmallFrom(arrayOne)
        right1 = getLargeFrom(arrayOne)
        left2 = getSmallFrom(arrayTwo)
        right2 = getLargeFrom(arrayTwo)

    return sameBsts(left1, left2) and sameBsts(right1, right2)


def getSmallFrom(left):
    smaller = []
    standard = left[0]
    for i in range(1, len(left)):
        if left[i] < standard:
            smaller.append(left[i])
    return smaller


def getLargeFrom(right):
    larger = []
    standard = right[0]
    for i in range(1, len(right)):
        if right[i] >= standard:
            larger.append(right[i])
    return larger





