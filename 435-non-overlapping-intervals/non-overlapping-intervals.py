class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x: x[1])
        count = 0
        end = float("-inf")

        for s, e in sorted_intervals:
            if end <= s:
                end = e
            else:
                count += 1
        
        return count