class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        st = set(nums)
        res = 0

        for i in st:
            if i-1 not in st:
                j = i+1
                c = 1
                while j in st:
                    c += 1
                    j += 1
                res = max(res, c)

        return res


