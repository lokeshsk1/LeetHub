class Solution:
    def compressedString(self, s: str) -> str:
        
        res = ""
        i = 0

        while i < len(s):
            c = 0
            curr = s[i]
            while i < len(s) and s[i] == curr:
                i += 1
                c += 1
            nines = c // 9
            rem = c % 9

            if c < 9:
                res += str(c) + curr
            else:
                for _ in range(nines):
                    res += '9' + curr
                if rem > 0:
                    res += str(rem) + curr
        
        return res
                

