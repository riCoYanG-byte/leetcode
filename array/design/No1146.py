# 实现支持下列接口的「快照数组」- SnapshotArray：
#
# SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
# void set(index, val) - 会将指定索引 index 处的元素设置为 val。
# int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
# int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
#
from bisect import bisect


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snapshot = [{0:0} for _ in range(length)]
        self.id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snapshot[index][self.id] = val

    def snap(self):
        self.id += 1
        return self.id - 1

    def get(self, index, snap_id):
        if snap_id in self.snapshot[index]:
            return self.snapshot[index][snap_id]
        else:
            key = bisect.bisect_left(list(self.snapshot[index].keys()))
            return self.snapshot[index][key]



    # Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
