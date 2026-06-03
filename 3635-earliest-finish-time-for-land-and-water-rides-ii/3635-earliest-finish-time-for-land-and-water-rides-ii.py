class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        res = float('inf')
        l = len(landStartTime)
        w = len(waterStartTime)

        minL, minW, res = float('inf'), float('inf'), float('inf')

        for i in range(l):
            minL = min(minL, landStartTime[i] + landDuration[i])
        
        for i in range(w):
            minW = min(minW, waterStartTime[i] + waterDuration[i])
        
        for i in range(w):
            res = min(res, max(minL, waterStartTime[i]) + waterDuration[i])

        for i in range(l):
            res = min(res, max(minW, landStartTime[i]) + landDuration[i])
        
        return res