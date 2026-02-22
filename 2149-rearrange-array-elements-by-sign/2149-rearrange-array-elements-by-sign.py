class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        res = []

        n = 0; p = 0

        while n < len(nums) and p < len(nums):

            while nums[n] >= 0:
                n += 1
            
            while nums[p] < 0:
                p += 1
            
            res.append(nums[p])
            res.append(nums[n])
            p += 1
            n += 1
        
        return res
