class Solution:
    def climbStairs(self, n: int) -> int:
        

        a = 1; b = 1

        #1 1 2 3 5 8

        for _ in range(n-1):
            a , b = b, a+b
        
        return b
