class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : x[1])
        
        res = 0
        lastNonOverlap = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[lastNonOverlap][1]:
                res += 1
            else:
                lastNonOverlap = i
                
        return res
        