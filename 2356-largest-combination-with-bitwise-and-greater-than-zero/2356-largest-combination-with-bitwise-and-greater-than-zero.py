class Solution:

    def largestCombination(self, nums: List[int]) -> int:

        res = 1
        bits = [0]*24

        for i in range(24):
            c = 0
            for n in nums:
                ith_bit = n >> i
                c += ith_bit & 1
            res = max(res, c)
        
        return res
