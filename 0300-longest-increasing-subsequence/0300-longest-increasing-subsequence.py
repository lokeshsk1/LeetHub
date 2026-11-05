class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [1] * n
        res = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

            res = max(res, dp[i])

        # print(dp) 
        return res
        
