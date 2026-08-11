class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.res = 0
        self.r = len(grid)
        self.c = len(grid[0])

        count = 0

        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 1:
                    count += 4
                    if i > 0 and grid[i-1][j] == 1:
                        count -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        count -= 2
                print(count)
        
        return count
                    

        
        