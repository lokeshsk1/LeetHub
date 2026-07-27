class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        dp = matrix
        res = 0

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] = int(dp[i][j])
                res = max(res, dp[i][j])

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if dp[i][j] == 0:
                    continue

                mn = min(dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1])
                
                dp[i][j] = mn + 1
            
                res = max(res, dp[i][j])

        print(dp)
        return res**2
        