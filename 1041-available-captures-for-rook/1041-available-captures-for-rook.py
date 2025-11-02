class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        res = 0
        m = len(board)
        n = len(board[0])

        I,J = (-1,-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    I,J = i,j

        
        dirs = ((0,1),(0,-1),(1,0),(-1,0))

        for x,y in dirs:
            u = I+x; v = J+y

            while 0<=u<m and 0<=v<n and board[u][v] != 'B':

                if board[u][v] == 'p':
                    res += 1
                    break
                
                u += x
                v += y
                
        
        return res