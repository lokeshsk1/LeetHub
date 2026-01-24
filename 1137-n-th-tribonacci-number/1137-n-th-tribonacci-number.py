class Solution:
    def tribonacci(self, n: int) -> int:
        
        a = 0; b = 1; c = 1

        for i in range(n):
            a, b, c = b, c, c+b+a
        
        return a