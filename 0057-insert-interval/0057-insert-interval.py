class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        n = newInterval
        
        for i in range(len(intervals)):
            
            if n[1] < intervals[i][0]:
                res.append(n)
                return res + intervals[i:] 
            elif n[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                n[0] = min(n[0], intervals[i][0])
                n[1] = max(n[1], intervals[i][1])

            print(res)
        
        res.append(n)
        return res

                



