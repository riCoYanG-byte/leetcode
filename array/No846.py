# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.

# 思路就是不断寻找最小的，然后恰好能把牌分没

import collections


def isNStraightHand(hand, W):
    count = collections.Counter(hand)
    while count:
        m = min(count)
        for k in range(m, m + W):
            v = count[k]
            if not v: return False
            if v == 1:
                del count[k]
            else:
                count[k] = v - 1

    return True


