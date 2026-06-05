"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        cached_start = 0
        cached_end = 0
        for i in intervals:
            start = i.start
            end = i.end
            if cached_end > start:
                return False
            cached_start = start
            cached_end = end
        return True