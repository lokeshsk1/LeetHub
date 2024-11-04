class Solution:
    def compressedString(self, s: str) -> str:
        
        res = ""
        i = 0

        while i < len(s):
            c = 0
            curr = s[i]
            while i < len(s) and s[i] == curr and c < 9:
                i += 1
                c += 1
            res += str(c) + curr
        
        return res
                

