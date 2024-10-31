class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0 for _ in range(n+1)]

        for i in range(2, n+1):
            for j in range(1, min(i,4)):
                dp[i] = max(dp[i], j * max(dp[i-j], i-j))

        return dp[n]


        