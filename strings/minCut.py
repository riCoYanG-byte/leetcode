def isPal(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


def palindromePartitioningMinCuts(string):
    # Write your code here.
    substrings = [[False for i in string] for j in string]
    for i in range(len(string)):
        for j in range(i, len(string)):
            substrings[i][j] = isPal(string[i:j + 1])
    cuts = [float("inf") for i in string]
    for i in range(len(string)):
        if substrings[0][i] is True:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if substrings[j][i] is True and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1

    return cuts[-1]


print(palindromePartitioningMinCuts("noonabbad"))
