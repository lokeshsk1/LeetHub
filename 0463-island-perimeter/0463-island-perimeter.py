class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.res = 0
        self.r = len(grid)
        self.c = len(grid[0])

        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 1:
                    self.dfs(grid,i,j)
        
        return self.res


    def dfs(self, grid, i, j):
        
        #top
        if i == 0 or (i-1 >= 0 and grid[i-1][j] == 0):
            self.res += 1

        #bottom
        if i == self.r-1 or (i+1 <= self.r and grid[i+1][j] == 0):
            self.res += 1

        #left
        if j == 0 or (j-1 >= 0 and grid[i][j-1] == 0):
            self.res += 1
        
        #right
        if j == self.c-1 or (j+1 >= 0 and grid[i][j+1] == 0):
            self.res += 1
            

