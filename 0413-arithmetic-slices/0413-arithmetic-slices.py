class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        
        n = len(nums)

        if n < 3:
            return 0

        dp = [0] * n

        if nums[1] - nums[0] == nums[2] - nums[1]:
            dp[2] = 1
        
        for i in range(3, n):
            if dp[i-1] and nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
            elif nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = 1

        print(dp)

        return sum(dp)
