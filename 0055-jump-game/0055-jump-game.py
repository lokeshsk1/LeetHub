class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        dp = [0]*len(nums)

        for i in range(len(nums)):

            if i > dp[i-1]:
                return False
            
            dp[i] = max(dp[i-1], i + nums[i])

            if dp[i] > len(nums)-1:
                return True

        
        return True