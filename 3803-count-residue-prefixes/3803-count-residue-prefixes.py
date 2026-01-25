class Solution:
    def residuePrefixes(self, s: str) -> int:
        
        res = 0
        uniq = set()

        for i in range(len(s)):
            uniq.add(s[i])

            if (i+1) % 3 == len(uniq):
                res += 1
            if len(uniq) > 2:
                break
        
        return res