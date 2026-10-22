class Solution:
    def climbStairs(self, n: int) -> int:
        
        p2, p1 = 0, 1

        for i in range(n):
            p2, p1 = p1, p2+p1
        

        return p1
        
