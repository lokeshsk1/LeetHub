class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        b = str(bin(n)[2:])

        print(b, len(b[1:]))

        return b[0] == '1' and all(i=='0' for i in b[1:]) and len(b[1:])%2==0

        