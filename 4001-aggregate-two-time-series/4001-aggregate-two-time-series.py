class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:

        p1 = 0 ; p2 = 0
        res = []

        while p1 < len(series1) and p2 < len(series2):
            
            tot = series1[p1][1] + series2[p2][1]
            
            time = min(series1[p1][0] , series2[p2][0])
            
            res.append([time, tot])

            if series1[p1][0] == time:
                p1 += 1
            if series2[p2][0] == time:
                p2 += 1

        if p1 >= len(series1):
            res += series2[p2:]
            
        if p2 >= len(series2):
            res += series1[p1:]

        return res