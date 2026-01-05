class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        res = 0
        m = len(matrix) ; n = len(matrix[0])
        negs = 0
        mini = float("inf")

        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    negs += 1
                mini = min(mini, abs(matrix[i][j]))
                res += abs(matrix[i][j])
        
        if negs % 2 != 0:
            res -= (mini * 2)
                
        return res

                    


