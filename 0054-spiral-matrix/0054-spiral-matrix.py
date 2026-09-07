class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix); n = len(matrix[0])

        sr = sc = 0
        er = m-1; ec = n-1
        res = []

        while sr<=er and sc<=ec:

            for i in range(sc, ec+1):
                res.append(matrix[sr][i])
            sr += 1

            for i in range(sr, er+1):
                res.append(matrix[i][ec])
            ec -= 1

            if sr<=er:
                for i in range(ec, sc-1, -1):
                    res.append(matrix[er][i])
                er -= 1

            if sc<=ec:
                for i in range(er, sr-1, -1):
                    res.append(matrix[i][sc])
                sc += 1
            
        print(res)
        return res
            
