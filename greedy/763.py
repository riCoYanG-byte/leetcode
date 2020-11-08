# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

# enumerate 有下标

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hashmap = {}
        for i,c in enumerate(S):
            hashmap[c] = i
        j,anchor = 0,0
        res = []
        for i, c in enumerate(S):
            j = max(j,hashmap[c])
            if i==j:
                res.append(i-anchor+1)
                anchor = i+1

        return res
