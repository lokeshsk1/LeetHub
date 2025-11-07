class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hset = set(nums)
        res = 0

        for i in hset:
            l = 1
            if i-1 not in hset:
                while i+1 in hset:
                    i += 1
                    l += 1
                res = max(res, l)
        
        return res
                