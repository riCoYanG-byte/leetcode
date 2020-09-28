# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In
# these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
#
# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications
# of the following extension operation: choose a group consisting of characters c, and add some number of characters
# c to the group so that the size of the group is 3 or more.
#
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get
# "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to
# get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two
# extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
#
# Given a list of query words, return the number of words that are stretchy.

# solution:
# 我们首先将 S 拆分成若干组相同的字母，并存储每组字母的长度。例如当 S 为 abbcccddddaaaaa 时，可以得到 5 组字母，它们分别为 abcda，长度为 [1, 2, 3, 4, 5]。
#
# 对于 words 中的每个单词 word，如果它可以扩张得到 S，那么它必须和 S 有相同的字母组。对于每一组字母，假设 S 中有 c1 个，word 中有 c2 个，那么会有下面几种情况：
#
# 如果 c1 < c2，那么 word 不能扩张得到 S；
#
# 如果 c1 >= 3，那么只要添加 c1 - c2 个字母即可；
#
# 如果 c1 < 3，由于在扩张时至少需要添加到 3 个字母，所以此时不能添加字母，必须有 c1 == c2。
#
# 如果 word 的包含的字母组中的每个字母都满足上述情况，那么 word 可以扩张得到 S。

def expressiveWords(S, words):
    count = 0
    for word in words:
        if canStrechy(S, word) is True:
            count += 1
    return count


def getKeyTable(str):
    table = []
    for ele in str:
        if not table:
            table.append([ele, 1])
        else:
            if ele == table[-1][0]:
                table[-1][1] += 1
            else:
                table.append([ele, 1])
    return table


def canStrechy(S, word):
    counter_S = getKeyTable(S)
    counter_word = getKeyTable(word)
    for i in range(len(S)):
        if len(counter_S) != len(counter_word):
            break
        if counter_S[i][0] != counter_word[i][0]:
            break
        if counter_S[i][1] < 3 and counter_S[i][1] != counter_word[i][1]:
            break
        if i == len(counter_S) - 1:
            return True
    return False


print(expressiveWords('helloo', ["hello"]))
