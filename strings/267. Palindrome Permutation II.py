import collections


class Solution:
    def __init__(self):
        self.res = []

    def generatePalindromes(self, s: str) -> List[str]:
        ## RC ##
        ## APPROACH : BACKTRACKING ##
        ## EDGE CASE : "aaaaaaa" (odd num) ##
        ## LOGIC ##
        ## 1. you can have utmost one char with odd freq, else return []
        ## 2. say for aabcccc, p = "b", take chars="acc" (only half of them), for all combinations of acc, append( combination + p + combination[::-1]) to result array

        ## TIME COMPLEXITY : O((N/2)!) ##
        ## SPACE COMPLEXITY : O(N) ##

        count = collections.Counter(s)
        p = ""
        chars = ""
        for ch in count.keys():
            if (count[ch] % 2 == 1):
                # edge case
                if (count[ch] > 1):
                    chars += ch * (count[ch] // 2)
                p += ch
            else:
                chars += ch * (count[ch] // 2)

        if len(p) > 1: return []

        def dfs(curr, s):
            if curr in visited:
                return
            if not s:
                self.res.append(curr + p + curr[::-1])
                return
            visited.add(curr)
            for i in range(len(s)):
                curr = curr + s[i]
                dfs(curr, s[:i] + s[i + 1:])
                curr = curr[:-1]

        visited = set()
        dfs("", chars)
        return self.res
