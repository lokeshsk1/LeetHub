class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(i):
            s = ""
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    s += board[i][j]

            return len(list(s))==len(set(list(s)))

        def checkCol(j):
            s = ""
            for i in range(len(board)):
                if board[i][j] != ".":
                    s += board[i][j]

            return len(list(s))==len(set(list(s)))


        def checkBox(i):
            r = (i//3) * 3 #3 for 3to5
            c = (i%3) * 3 # 0,3,6 -> 0

            s = ""
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if board[i][j] != ".":
                        s += board[i][j]

            return len(list(s))==len(set(list(s)))

        res = True
        for i in range(9):
            if not (checkRow(i) and checkCol(i) and checkBox(i)):
                return False
        return True
        
        

        