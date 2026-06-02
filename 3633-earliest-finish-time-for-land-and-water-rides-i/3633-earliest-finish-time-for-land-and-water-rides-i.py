class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        res = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                totL = landStartTime[i] + landDuration[i]
                if waterStartTime[j] > totL:
                    totL += (waterStartTime[j] - totL)
                totL += waterDuration[j]
                res = min(res, totL)
        
        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                totW = waterStartTime[i] + waterDuration[i]
                if landStartTime[j] > totW:
                    totW += (landStartTime[j] - totW)
                totW += landDuration[j]
                res = min(res, totW)
            
        return res