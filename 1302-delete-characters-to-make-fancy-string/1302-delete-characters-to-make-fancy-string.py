class Solution:
    def makeFancyString(self, s: str) -> str:

        res = s[:2]

        for i in range(2, len(s)):
            if not res[-1] == res[-2] == s[i]:
                res += s[i]
        
        return res


        