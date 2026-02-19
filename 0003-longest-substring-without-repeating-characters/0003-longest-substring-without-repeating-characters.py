class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = dict()
        start = 0
        res = 0

        for i,e in enumerate(s):

            if e in hmap:
                start = max(start, hmap[e] + 1)

            res = max(res, i - start + 1)

            hmap[e] = i
        
        return res


            