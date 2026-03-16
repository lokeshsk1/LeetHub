class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        vis = dict()
        last = 0
        res = 0

        for i,e in enumerate(s):
            if e in vis:
                last = max(last, vis[e] + 1)
            vis[e] = i

            res = max(res, i - last + 1)

        return res