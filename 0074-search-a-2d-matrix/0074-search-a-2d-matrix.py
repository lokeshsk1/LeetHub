class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = len(matrix); c = len(matrix[0])

        l = 0; h = (r*c)-1

        while l <= h:

            mid = l + (h-l)//2

            if matrix[mid//c][mid%c] == target:
                return True
            elif matrix[mid//c][mid%c] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return False