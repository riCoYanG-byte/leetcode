def interweavingStrings(one, two, three):
    # Write your code here.
    if len(one) + len(two) != len(three):
        return False
    return checkInter(one, two, three, 0, 0)


# a b ab
# 0 0 0
# 1 0 1
# 0 1 1
def checkInter(one, two, three, i, j):
    k = i + j
    # 这个是走到最后检测空的情况、因为是从0开始走的
    if k == len(three):
        return True
    if i < len(one) and one[i] == three[k]:
        if checkInter(one, two, three, i + 1, j):
            return True
    if j < len(two) and two[j] == three[k]:
        if checkInter(one, two, three, i, j + 1):
            return True

    return False


print(interweavingStrings('a', 'b', 'ac'))
