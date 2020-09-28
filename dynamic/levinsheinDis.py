def levenshteinDistance(str1, str2):
    # Write your code here.
    edit = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        edit[i][0] = edit[i - 1][0] + 1
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edit[i][j] = edit[i - 1][j - 1]
            else:
                edit[i][j] = min(edit[i - 1][j], edit[i][j - 1], edit[i - 1][j - 1]) + 1

    return edit[-1][-1]


print(levenshteinDistance("a", "bc"))
