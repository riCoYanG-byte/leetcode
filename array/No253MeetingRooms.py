# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals:
        return 0
    start_time = []
    end_time = []
    for meeting in intervals:
        start_time.append(meeting[0])
        end_time.append(meeting[1])
    start_time.sort()
    end_time.sort()

    usedRoom = 0
    st = 0
    et = 0
    while st < len(start_time):
        if start_time[st] > end_time[et]:
            usedRoom -= 1
            et += 1
        usedRoom += 1
        st += 1

    return usedRoom


print(minMeetingRooms([[7, 10], [2, 4]]))

print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
