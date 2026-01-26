class Solution:
    def findValidPair(self, s: str) -> str:
        
        c = Counter(s)

        for i in range(1, len(s)):
            if s[i] != s[i-1] and c[s[i]] == int(s[i]) and c[s[i-1]] == int(s[i-1]):
                return s[i-1] + s[i]

        return ""