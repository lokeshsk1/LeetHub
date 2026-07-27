class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max1 = max(nums[0], nums[1])
        max2 = min(nums[0], nums[1])

        for i in nums[2:]:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
            
        return (max1-1) * (max2-1)