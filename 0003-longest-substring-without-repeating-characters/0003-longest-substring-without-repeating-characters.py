class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        hmap = {}
        res = 0

        for i in range(len(s)):

            if s[i] in hmap:
                l = max(l, hmap[s[i]] + 1)

            res = max(res, i-l+1)
            hmap[s[i]] = i
            print(i,l)
        
        return res



            
