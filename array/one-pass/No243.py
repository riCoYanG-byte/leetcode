#
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1

# one passsolution :
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = -1, -1
        minDis = float('inf')
        for i in range(len(words)):
            if word1 == words[i]:
                w1 = i
            elif word2 == words[i]:
                w2 = i
            if w1 != -1 and w2 != -1:
                minDis = min(abs(w2 - w1), minDis)
        return minDis

