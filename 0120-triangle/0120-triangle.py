class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = triangle
        r = len(dp)
        c = len(dp[0])

        for i in range(1, r):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] += dp[i-1][j]
                elif j == len(dp[i])-1:
                    dp[i][j] += dp[i-1][j-1]
                else:
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j])

        return min(dp[-1])
        