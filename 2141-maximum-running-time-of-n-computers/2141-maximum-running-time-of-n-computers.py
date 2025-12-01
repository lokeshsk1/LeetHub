class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        batteries.sort()
        tot = sum(batteries)
    
        while batteries[-1] > tot // n:
            n -= 1
            tot -= batteries.pop()
        
        return tot // n
