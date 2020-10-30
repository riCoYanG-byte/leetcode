# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """


# first solution to scan each  row and remember its smallest digit
# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         rows, cols = binaryMatrix.dimensions()
#         smallest_index = cols
#         # Go through each of the rows.
#         for row in range(rows):
#             # Linear seach for the first 1 in this row.
#             for col in range(cols):
#                 if binaryMatrix.get(row, col) == 1:
#                     smallest_index = min(smallest_index, col)
#                     break
#         # If we found an index, we should return it. Otherwise, return -1.
#         return -1 if smallest_index == cols else smallest_index

#  second solution is  use  the binary search

# In summary, if the middle element is a:
#
# 0, then the target must be to the right.
# 1, then the target is either this element or to the left.

# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         rows, cols = binaryMatrix.dimensions()
#         smallest_index = cols
#         for row in range(rows):
#             # Binary Search for the first 1 in the row.
#             lo = 0
#             hi = cols - 1
#             while lo < hi:
#                 mid = (lo + hi) // 2
#                 if binaryMatrix.get(row, mid) == 0:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             # If the last element in the search space is a 1, then this row
#             # contained a 1.最后是一定找到1 的时候才会更新
#             if binaryMatrix.get(row, lo) == 1:
#                 smallest_index = min(smallest_index, lo)
#         # If smallest_index is still set to cols, then there were no 1's in
#         # the grid.
#         return -1 if smallest_index == cols else smallest_index

# 最佳方法top-down search
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        rows, cols = binaryMatrix.dimensions()

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1
































