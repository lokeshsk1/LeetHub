class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        pq = []

        for i in range(len(matrix[0])):
            heapq.heappush(pq, (matrix[0][i], (0,i)))
        
        for i in range(k-1):
            val,xy = heapq.heappop(pq)
            x,y = xy
            if x+1 < len(matrix):
                heapq.heappush(pq, (matrix[x+1][y], (x+1, y)))
        
        resi, resj = pq[0][1]
        return matrix[resi][resj]

        