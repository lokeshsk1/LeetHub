class Solution:
    def climbStairs(self, n: int) -> int:
        
        p1, p2 = 1, 2

        for i in range(n-1):
            p1, p2 = p2, p1 + p2
        
        return p1