# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

import collections
from collections import defaultdict


def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    # 构建intermedia word
    intermediaList = defaultdict(list)
    for word in wordList:
        for i in range(0, len(word)):
            key = word[:i] + '*' + word[i + 1:]
            value = word
            intermediaList[key].append(value)
    print(intermediaList)

    # bfs遍历
    # 相当于通过中间状态bfs
    queue = collections.deque(beginWord, 1)  # word,level
    while queue:
        currentWord, level = queue.popleft()
        for i in range(len(currentWord)):
            inter = currentWord[:i] + '*' + currentWord[i + 1:]
            for word in intermediaList[inter]:
                if word == endWord:
                    return level + 1
                queue.append(word)
            intermediaList[inter] = []


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
