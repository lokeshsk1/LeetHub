class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        mat = [[0]*n for _ in range(m)]
        mat[0][0] = 1

        for i in range(m):
            for j in range(n):
                tot = 0
                if i-1 >= 0:
                    mat[i][j] += mat[i-1][j]
                if j-1 >= 0:
                    mat[i][j] += mat[i][j-1]
        
        print(mat)
        return mat[-1][-1]

        