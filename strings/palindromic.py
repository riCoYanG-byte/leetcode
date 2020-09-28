def longestPalindromicSubstring(string):
    # Write your code here.
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPa(string, i - 1, i + 1)
        even = getLongestPa(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]+1]


def getLongestPa(string, leftidx, rightidx):
    left = leftidx
    right = rightidx
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        else:
            left = left - 1
            right = right + 1

    return [left + 1, right-1]


print(longestPalindromicSubstring("aba"))
