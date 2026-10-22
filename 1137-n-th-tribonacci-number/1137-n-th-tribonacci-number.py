class Solution:
    def tribonacci(self, n: int) -> int:
        
        p3, p2, p1 = 0, 0, 1

        for i in range(n):
            p3, p2, p1 = p2, p1, p1+p2+p3
        
        return p2

        # 0, 0, 1, 1, 2, 4