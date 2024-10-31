class Solution:
    def integerBreak(self, n: int) -> int:

        res = 1

        if n < 4:
            return n-1

        while n > 4:
            res *= 3
            n -= 3
        
        res *= n
        
        return res



        