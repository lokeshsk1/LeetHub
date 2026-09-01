class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            if 0<=i<r and 0<=j<c and grid[i][j] == "1":
                grid[i][j] = "0"
            
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i-1, j)
        
        res = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        

        return res