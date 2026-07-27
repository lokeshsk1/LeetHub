class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp = obstacleGrid

        if dp[0][0] == 1 or dp[-1][-1] == 1:
            return 0
 
        m = len(dp)
        n = len(dp[0])

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 1:
                    dp[i][j] = 'X'
        
        dp[0][0] = 1
        # print(dp)

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 'X':
                    continue
                if i>0 and dp[i-1][j] != 'X':
                    dp[i][j] = dp[i-1][j]
                if j > 0 and dp[i][j-1] != 'X':
                    dp[i][j] += dp[i][j-1]
                
        # print(dp)
        
        return dp[-1][-1]

        
        