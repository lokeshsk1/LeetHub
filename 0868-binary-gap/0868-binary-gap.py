class Solution:
    def binaryGap(self, n: int) -> int:
        
        b = bin(n)[2:]
        prev1 = -1
        res = 0

        for i,e in enumerate(b):
            
            if prev1 != -1 and e == '1':
                res = max(res, i - prev1)

            if e == '1':
                prev1 = max(prev1, i)

        return res
