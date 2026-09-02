class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        r = len(board)
        c = len(board[0])

        def dfs(i, j):

            if i >= 0 and i <= r-1 and j >= 0 and j <= c-1 and board[i][j] == "O" :
                
                board[i][j] = "#"
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
                    

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and i == 0 or i == r-1 or j == 0 or j == c-1:
                    print("*")
                    dfs(i,j)
        

        for i in range(r):
            for j in range(c):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        
        
