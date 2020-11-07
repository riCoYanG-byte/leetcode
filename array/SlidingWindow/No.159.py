# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):

        if len(s) < 3:
            return len(s)

        left, right, max_len = 0, 0, 2
        hashmap = defaultdict()

        while right < len(s):
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1
            if len(hashmap) == 3:
                min_value = min(hashmap.values())
                del hashmap[s[min_value]]
                left = min_value + 1

            max_len = max(max_len, right - left)

        return max_len

