# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}

        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                next_greater[stack.pop()] = n
            stack.append(n)

        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[n] for n in nums1]