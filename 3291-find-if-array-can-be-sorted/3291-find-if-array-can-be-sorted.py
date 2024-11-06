class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        bits = []

        for i in nums:
            setbits = self.count_set_bits(i)
            bits.append(setbits)
        
        i = 0
        prev_max = None

        while i < len(bits):
        
            curr = i
            mx = nums[curr]
            mn = nums[curr]
            i += 1
            
            while i < len(bits) and bits[i] == bits[curr]:
                mx = max(mx, nums[i])
                mn = min(mn, nums[i])
                i += 1

            if prev_max and mn < prev_max:
                return False

            prev_max = mx

        return True


    def count_set_bits(self, n):
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


        