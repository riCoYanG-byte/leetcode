def isMonotonic(array):
    # Write your code here.
    if len(array) < 2:
        return True
    for i in range(len(array) - 1):
        direction = array[i + 1] - array[i]
        if direction != 0:
            break
        else:
            continue
    for j in range(len(array) - 1):
        if isTrend(direction, array[j], array[j + 1]):
            continue
        else:
            return False
    return True


def isTrend(direction, current, next):
    currentTrend = next - current
    if currentTrend * direction > 0:
        return True
    elif currentTrend * direction == 0:
        return True
    else:
        return False


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
