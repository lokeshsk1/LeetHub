class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = len(matrix); c = len(matrix[0])

        m = r-1; n = 0

        while m >= 0 and n < c:

            if matrix[m][n] == target:
                return True
            if matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        
        return False

