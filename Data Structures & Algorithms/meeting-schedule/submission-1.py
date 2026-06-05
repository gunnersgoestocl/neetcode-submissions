"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: -x.end)
        l = len(intervals)
        if l == 0:
            return True
        def _canAttendMeetings(start, end, i):
            # check if meeting i can fit into start to end
            # not fit return False
            # if fit return its child
            if i >= l:
                return True
            mtg_start = intervals[i].start
            mtg_end = intervals[i].end
            if start <= mtg_start and mtg_end <= end:
                return _canAttendMeetings(start, mtg_start, i+1) or _canAttendMeetings(mtg_end, start, i+1)
            else:
                return False


        return _canAttendMeetings(0, intervals[0].end, 0)
