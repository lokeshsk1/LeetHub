class Solution:

    def largestCombination(self, nums: List[int]) -> int:

        bits = [0]*24

        for i in nums:
            c = 0
            while i:
                bits[c] += i & 1
                i >>= 1
                c += 1
        
        print(bits)
        return max(bits)
