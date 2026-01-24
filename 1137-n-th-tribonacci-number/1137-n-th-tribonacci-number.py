class Solution:
    def tribonacci(self, n: int) -> int:
        
        p3 = 0; p2 = 1; p1 = 1

        for i in range(n):
            p3, p2, p1 = p2, p1, p3+p2+p1
        
        return p3