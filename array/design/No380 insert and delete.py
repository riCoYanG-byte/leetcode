# Implement the RandomizedSet class:
#
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# Follow up: Could you implement the functions of the class with each function works in average O(1) time?


# tips

# Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.

# using a list can get a constant time

from random import choice
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        # append length 相当于 idx
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # swap
        if val in self.dict:
            last_ele, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_ele] = last_ele, idx
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()