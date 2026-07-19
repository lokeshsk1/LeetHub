class Solution:
    def numSquares(self, n: int) -> int:
        
        ps = []

        i = 1
        while i*i <= n:
            ps.append(i*i)
            i += 1
        
        ps = set(ps)

        dp = [n+1] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in ps:
                dp[i] = min(dp[i], dp[i-j]+1)

        return dp[n]