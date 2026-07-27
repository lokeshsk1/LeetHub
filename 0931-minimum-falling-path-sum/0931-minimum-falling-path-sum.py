class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = matrix

        r = len(dp); c = len(dp[0]) 

        for i in range(1, r):
            for j in range(c):
                if j == 0:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j+1])
                elif j == c-1:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
        
        return min(dp[-1])

        