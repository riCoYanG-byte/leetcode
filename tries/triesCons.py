# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            self.build(i, string)

    def build(self, i, string):
        current = self.root

        for j in range(i, len(string)):

            letters = string[j]
            if letters not in current:
                current[letters] = {}
            current = current[letters]
        current[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                return False
            current = current[string[i]]
        return self.endSymbol in current
