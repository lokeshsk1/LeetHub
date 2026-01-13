class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        r = len(matrix)
        c = len(matrix[0])
        pre = [[0]*(c+1) for _ in range(r+1)]

        for i in range(1, r+1):
            for j in range(1, c+1):
                pre[i][j] = pre[i][j-1] + pre[i-1][j] + matrix[i-1][j-1] - pre[i-1][j-1]
        
        self.pre = pre
        print(pre)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        full = self.pre[row2+1][col2+1]
        vert = self.pre[row2+1][col1]
        hori = self.pre[row1][col2+1]
        diag = self.pre[row1][col1]
        return full - vert - hori + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)