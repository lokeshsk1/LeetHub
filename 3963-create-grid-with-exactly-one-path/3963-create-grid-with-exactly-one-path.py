class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        res = []

        for i in range(m):
            st = ""
            for j in range(n):
                if i == 0 or j == n-1:
                    st += '.'
                else:
                    st += '#'
            res.append(st)
        
        return res


