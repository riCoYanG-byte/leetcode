# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class DoubleLinklist(object):
    pass


class DoubleListNode(object):
    pass


class LRUCache:

    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.cache = {}
        self.mostRecentNode = DoubleLinklist()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictleastRecent(key, value)
            else:
                self.currentSize += 1
                self.addrecentUse(key, value)
            self.cache[key] = DoubleListNode(key,value)
        else:
            self.replaceKeyfromAdd(key, value)
        self.updateMostRecentNode(self.cache[key])

    def getValueFromKey(self, key):
        # Write your code here.
        self.updateMostRecentNode(self)
        return self.cache[key].value

    def getMostRecentKey(self):
        # Write your code here.
        return self.mostRecentNode.head.key

    def evictleastRecent(self, key, value):
        keyToRemove = self.mostRecentNode.tail.key
        del self.cache[keyToRemove]

    def addrecentUse(self, key, value):
        self.cache[key] = value

    def updateMostRecentNode(self):
        self.mostRecentNode.setHead(self)
