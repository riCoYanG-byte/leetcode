def reorganizeString(S):
    N = len(S)
    A = []
    # 如果字母c大于 N+1/2 插空是肯定插入不了的
    for c, x in sorted((S.count(x), x) for x in set(S)):
        if c > (N + 1) / 2: return ""
        A.extend(c * x)
    ans = [None] * N

    # 做了个交叉
    ans[::2], ans[1::2] = A[N / 2:], A[:N / 2]
    return "".join(ans)