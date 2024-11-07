class Solution:

    def largestCombination(self, nums: List[int]) -> int:

        res = 1
        bits = [0]*24 #10^7 has 24 bits

        for i in range(24):
            set_bits_at_ith_position = 0
            for n in nums:
                ith_bit = n >> i
                set_bits_at_ith_position += ith_bit & 1
            res = max(res, set_bits_at_ith_position)
        
        return res