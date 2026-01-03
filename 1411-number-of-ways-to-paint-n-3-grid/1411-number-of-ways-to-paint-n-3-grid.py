class Solution:
    def numOfWays(self, n: int) -> int:
        
        MOD = (10**9)+7
        color3 = 6
        color2 = 6

        for i in range(2, n+1):
            temColor3 = color3
            color3 = ((color3 * 2) + (color2 * 2)) % MOD
            color2 = ((temColor3 * 2) + (color2 * 3)) % MOD

        return ( color3 + color2 ) % MOD


        # R G B = 

        # B R G 
        # G B R

        # +

        # G R G
        # G B G

        # ---------

        # R B R = 

        # G R B
        # B R G

        # +

        # G R G
        # B R B
        # B G B





