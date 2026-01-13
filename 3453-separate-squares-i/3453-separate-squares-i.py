class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        miny = maxy = squares[0][1]
        tot = 0

        for x,y,l in squares:
            tot += l*l
            miny = min(miny, y)
            maxy = max(maxy, y+l)
        
        halfArea = tot / 2
        
        for i in range(100):
            mid = miny + (maxy - miny) / 2

            if self.calculateArea(squares, mid) >= halfArea:
                maxy = mid
            else:
                miny = mid

        return maxy

    def calculateArea(self, squares, currY):

        area = 0

        for x,y,l in squares:
            top = y + l

            if y >= currY:
                continue
            elif top <= currY:
                area += l*l
            else:
                area += (currY - y) * l
        
        return area




        