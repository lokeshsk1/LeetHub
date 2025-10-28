class Solution:
    def convert(self, s: str, n: int) -> str:
        

        # PAYPALISHIRING
        # 1 5 9 13 
        # 2 4 6 8 10 12 14
        # 3 7 10

        # P.    H
        # A.   S
        # Y.  I
        # P. L
        # A

        # 1 5
        # 1 7
        # 1 9

        if n == 1:
            return s

        res = ""

        k1 = 2*n - 2
        k2 = k1 - 2

        for i in range(0, len(s), k1):
            res += s[i]

        for i in range(1,n-1):

            for j in range(i, len(s), k1):

                res += s[j]
                if j+k2 < len(s):
                    res += s[j+k2]
            
            k2 -= 2

        for i in range(n-1, len(s), k1):
            res += s[i]

        return res