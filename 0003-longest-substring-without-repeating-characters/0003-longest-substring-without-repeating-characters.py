class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        vis = set()
        left = 0
        res = 0

        for i,e in enumerate(s):
            print(left, i)
            if e not in vis:
                res = max(res, i - left + 1)
            else:
                while e in vis:
                    vis.remove(s[left])
                    left += 1
            vis.add(e)

        return res