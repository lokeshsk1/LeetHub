class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)-2, 3):
            if nums[i] in (nums[i+1], nums[i+2]):
                return nums[i]
            if nums[i+1] == nums[i+2]:
                return nums[i+1]
        
        return nums[-1]
            