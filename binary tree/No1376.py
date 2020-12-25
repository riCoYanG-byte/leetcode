# 剪枝法

def numOfMinutes(n, headID, manager, informTime):
    res = 0
    for i in range(len(manager)):
        if informTime[i] == 0:
            temp = 0
            index = i
            while index != -1:
                temp += informTime[index]
                index = manager[index]
            res = max(res, temp)
    return res


# Dfs


class Solution:
    total = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tmp = defaultdict(list)

        for i in range(len(manager)):
            tmp[manager[i]].append(i)

        self.dfs(tmp, informTime, headID, 0)
        return self.total

    def dfs(self, tmp, informTime, head_id, total):
        if not tmp[head_id]:
            self.total = max(self.total, total)

        for id_ in tmp[head_id]:
            self.dfs(tmp, informTime, id_, total + informTime[head_id])


# bfs

from collections import defaultdict
from queue import Queue


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        q = Queue()
        tmp = defaultdict(list)

        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            tmp[manager[i]].append(i)

        q.put((headID, 0))

        result = 0

        while not q.empty():
            this_id, val = q.get()

            for id_ in tmp[this_id]:
                q.put((id_, val + informTime[this_id]))
                result = max(result, val + informTime[this_id])

        return result
