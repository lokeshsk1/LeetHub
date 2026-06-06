class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:

        bulbs = math.ceil(brightness / 3)

        intervals.sort()
        
        res = []

        for i,j in intervals:
            if res and i <= res[-1][1]+1:
                res[-1][1] = max(res[-1][1], j)
            else:
                res.append([i,j])

        tot_time = sum(j-i+1 for i,j in res)

        return tot_time * bulbs
                