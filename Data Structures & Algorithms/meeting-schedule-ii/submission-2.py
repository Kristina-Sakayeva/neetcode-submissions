import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        rooms = []
        for interval in intervals:
            start, end = interval.start, interval.end

            if not rooms:
                rooms.append(end)
                continue
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)


        return len(rooms)

        