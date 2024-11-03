class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0

        r = len(grid); c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    grid[i][j] = -1

        grid[0][0] = 1

        for i in range(r):
            for j in range(c):
                if grid[i][j] != -1:
                    if i > 0 and grid[i-1][j]!=-1:
                        grid[i][j] += grid[i-1][j]
                    if j > 0 and grid[i][j-1]!=-1:
                        grid[i][j] += grid[i][j-1]
        

        return grid[-1][-1]
        