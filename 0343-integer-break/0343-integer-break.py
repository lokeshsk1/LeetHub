class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [1]*(n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(i+1):
                dp[i] = max(dp[i], max(i-j, dp[i-j]) * j)
        
        return dp[n]
