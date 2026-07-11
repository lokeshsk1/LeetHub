class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxTil = 0

        for i in range(len(nums)):
            
            if i > maxTil:
                return False
            maxTil = max(maxTil, i + nums[i])

        return True
