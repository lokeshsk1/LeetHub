class Solution:
    def residuePrefixes(self, s: str) -> int:
        
        res = 0
        pre = ""

        for i in s:
            pre += i

            if len(pre) % 3 == len(list(set(pre))):
                res += 1
        
        return res