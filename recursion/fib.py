def getNthFib(n):
    lastTwo = [0, 1]
    if n == 1:
        return lastTwo[0]
    if n == 2:
        return lastTwo[1]
    else:
        counter = 3
        while counter <= n:
            result = lastTwo[0] + lastTwo[1]
            # 赋值要有顺序
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = result
            counter += 1
        return result


print(getNthFib(4))
