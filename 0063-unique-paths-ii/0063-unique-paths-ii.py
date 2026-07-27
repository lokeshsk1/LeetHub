class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 1:
                    dp[i][j] = 'X'

        if dp[0][0] != 'X':
            dp[0][0] = 1 

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 'X':
                    continue
                if i>0 and dp[i-1][j] != 'X':
                    dp[i][j] = dp[i-1][j]
                if j > 0 and dp[i][j-1] != 'X':
                    dp[i][j] += dp[i][j-1]
                
        print(dp)
        
        return 0 if dp[-1][-1] == 'X' else dp[-1][-1]

        
        