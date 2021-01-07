import re 
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.pos = 0
        self.cha = re.compile(r'[a-zA-Z]+').findall(compressedString)
        print(self.cha)
        self.count = list(map(int, re.compile(r'[0-9]+').findall(compressedString)))

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext() is False:
            return ''
        self.count[self.pos] -= 1
        res = self.cha[self.pos]
        if self.count[self.pos] == 0:
            self.pos += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos != len(self.cha)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()