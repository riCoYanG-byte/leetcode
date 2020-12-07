# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
# 跟insert interval有点像

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Sort the intervals by their starting value (x[0])
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = []
        #Iterate through the sorted list of lists
        #If the ending time of the current block is greater then the starting time
        #of the next block then we return false
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        #Else if that statement was never triggered we return true
        return True