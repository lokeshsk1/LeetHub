class Solution:
    def maxDifference(self, s: str) -> int:
        
        c = Counter(s)
        oMax = 0
        eMin = float('inf')

        for i,j in c.items():
            if j%2:
                oMax = max(oMax, j)
            else:
                eMin = min(eMin, j)

        return oMax - eMin