# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

# bfs 检测路径上的线路是否在deadends中，是则切换路径，不是就add进来，时间复杂度略高

import collections

def getNeighbor(node):
    neiList = []
    for i in range(4):
        x = int(node[i])
        for d in (-1, 1):
            y = (x + d) % 10
            neiList.append(node[:i] + str(y) + node[i + 1:])
    return neiList

def openLock(deadends, target):
    # dead = set(deadends)
    queue = collections.deque([('0000', 0)])
    while queue:
        node, level = queue.popleft()
        if node in deadends:
            continue
        if node == target: return level
        tempNeighbor = getNeighbor(node)
        for nei in tempNeighbor:
            queue.append(nei, level + 1)
    return -1
