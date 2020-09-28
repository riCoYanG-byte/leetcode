# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getCurrentLevel(topAncestor, descendant):
    level = 0
    while descendant != topAncestor:
        descendant = descendant.ancestor
        level += 1
    return level


def commonAncestor(topAncestor, descendantHigher, descendantLower,diff):

    while diff > 0:
        descendantLower = descendantLower.ancestor
        diff -= 1

    while descendantLower != descendantHigher:
        descendantLower = descendantLower.ancestor
        descendantHigher = descendantHigher.ancestor

    return descendantLower


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    currentLevelone = getCurrentLevel(topAncestor, descendantOne)
    currentLeveltwo = getCurrentLevel(topAncestor, descendantTwo)
    diff = abs(currentLevelone-currentLeveltwo)

    if currentLevelone > currentLeveltwo:
        return commonAncestor(topAncestor, descendantOne, descendantTwo,diff)
    else:
        return commonAncestor(topAncestor, descendantTwo, descendantOne,diff)
