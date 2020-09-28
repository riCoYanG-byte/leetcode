# 给出一个单词列表，其中每个单词都由小写英文字母组成。
#
# 如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。
#
# 词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。
#
# 从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
#

# 因为单词不确定，所以逆向开始推算好一些

def longestStrChain(words):

    words.sort(key=len)
    note = {}
    maxChain = 1
    for word in words:
        if word not in note:
            note[word] = 1
        for i in range(len(word)):
            compare = word[:i] + word[i + 1:]
            if compare in note:
                note[word] = max(note[word], note[compare] + 1)
                maxChain = max(note[word], maxChain)

    return maxChain


