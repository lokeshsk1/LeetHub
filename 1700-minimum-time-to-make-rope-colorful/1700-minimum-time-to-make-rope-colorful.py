class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        res = 0
        cons = []

        i = 1
        while i < len(colors):
            while i<len(colors) and colors[i] == colors[i-1]:
                cons.append(neededTime[i-1])
                i += 1
            if len(cons) >= 1:
                cons.append(neededTime[i-1])
                res += sum(cons)
                res -= max(cons)
                print(cons)
                cons = []
            
            i += 1
        
        return res
