class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] = LIS till index i

        # dp[i] depends on dp[0:i]
        # dp[i] = max(dp[0:i]) + 1

        n = len(nums)
        dp = [1]*n

        res = 1
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])
        
        print(dp)

        return res
