class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        r = len(grid); c = len(grid[0])

        for i in range(r):
            for j in range(c):
                top = float(inf)
                left = float(inf)
                if i > 0:
                    top = grid[i-1][j]
                if j > 0:
                    left = grid[i][j-1]
                if not (top == float(inf) and left == float(inf)):
                    grid[i][j] += min(top, left)
        
        print(grid)
        return grid[-1][-1]


        