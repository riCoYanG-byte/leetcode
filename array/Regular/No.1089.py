# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        index =0
        length = len(arr)

        while index < length:
            if arr[index] == 0:
                arr.pop()
                arr.insert(index,0)
                index += 1
            index += 1
