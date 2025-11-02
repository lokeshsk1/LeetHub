class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        self.m = m; self.n = n
        grid = list(['N'] * n for _ in range(m))
        res = 0
        
        # print(grid)

        for i,j in guards:
            grid[i][j] = 'G'
        for i,j in walls:
            grid[i][j] = 'W'

        # print(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'G':
                    self.dfs(i,j,grid)

        print(grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'N':
                    res += 1
            
        return res

    def dfs(self, i, j, grid):

        m = self.m
        n = self.n

        dirs = ((0,1),(1,0),(-1,0),(0,-1))

        for x,y in dirs:
            u,v = i+x, j+y

            while 0<=u<m and 0<=v<n and grid[u][v] not in 'GW':
                grid[u][v] = 'Y'
                u += x
                v += y

        
                

