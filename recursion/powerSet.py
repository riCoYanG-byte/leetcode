# [1,2,3]
# [],[1],[2],[1,2]
# 对于每个子串都添加上了一个新的元素

def powerset(array):
    Set = [[]]
    for element in array:
        for subsetidx in range(len(Set)):
            current = Set[subsetidx]
            Set.append(current + [element])
    return Set

