class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # for i in grid:
        #     print(i, end='\n')

        r = len(grid)
        c = len(grid[0])

        i = r-1 ; j = 0
        res = 0

        while i>=0 and j<=c-1:
            if grid[i][j] < 0:
                res += c-j
                i -= 1
            else:
                j += 1
        
        return res