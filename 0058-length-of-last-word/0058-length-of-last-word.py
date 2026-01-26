class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()
        i = len(s)-1
        l = 0

        while i>=0 and s[i] != " ":
            i -= 1
            l += 1
        
        return l
