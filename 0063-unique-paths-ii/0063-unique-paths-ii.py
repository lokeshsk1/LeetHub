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
                    if i == 0:
                        for k in range(j, n):
                            dp[0][k] = 'X'
                    if j == 0:
                        for k in range(i, m):
                            dp[k][0] = 'X'

        print(dp)

        for i in range(m):
            for j in range(n):
                
                if dp[i][j] == 'X':
                    continue
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                elif dp[i-1][j] == 'X':
                    dp[i][j] = dp[i][j-1]
                elif dp[i][j-1] == 'X':
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        print(dp)
        
        return 0 if dp[-1][-1] == 'X' else dp[-1][-1]

        
        