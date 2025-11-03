class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        res = 0
        tot_time = 0
        max_time = 0

        i = 1
        while i < len(colors):
            while i<len(colors) and colors[i] == colors[i-1]:
                tot_time += neededTime[i-1]
                max_time = max(max_time, neededTime[i-1])
                i += 1
                
            tot_time += neededTime[i-1]
            max_time = max(max_time, neededTime[i-1])

            res += (tot_time - max_time)
            tot_time = max_time = 0
            
            i += 1
        
        return res
