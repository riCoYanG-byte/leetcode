# 不断比对结果进行交换就完事了

def moveElementToEnd(array, toMove):
    # Write your code here.
    start = 0
    end = len(array) - 1
    while start < end:
        while array[end] == toMove:
            end = end - 1

        if start > end:
            break

        if array[start] == toMove:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp
            start = start + 1
            end = end - 1
        else:
            start = start + 1
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
