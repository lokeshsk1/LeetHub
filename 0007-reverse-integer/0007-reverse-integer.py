class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        neg = False
        if x < 0:
            neg = True
            x *= -1

        while x:
            res = (res * 10) + x%10
            x //= 10
        
        if res >= 2**31:
            return 0
        if neg:
            res *= -1
        return res
