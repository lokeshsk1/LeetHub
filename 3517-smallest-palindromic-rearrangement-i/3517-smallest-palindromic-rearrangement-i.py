class Solution:
    def smallestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        s1 = s[:len(s)//2]
        sort_s1 = "".join(sorted(s1))

        res = ""

        if len(s) % 2 == 0:
            res = sort_s1 + sort_s1[::-1]
        else:
            res = sort_s1 + s[(len(s)//2)] + sort_s1[::-1]

        return res