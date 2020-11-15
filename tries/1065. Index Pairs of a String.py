# Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """

        # build a trie
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter in node:
                    node = node[letter]
                else:
                    node[letter] = {}
                    node = node[letter]
            # end symbol of trie
            node['#'] = '#'

        # searching the trie
        res = []

        for startidx in range(len(text)):
            node = trie
            endidx = startidx
            while text[endidx] in node:
                node = node[text[endidx]]
                endidx += 1
                if '#' in node:
                    res.append([startidx,endidx])
                if endidx > len(text):

                    break
        return res



