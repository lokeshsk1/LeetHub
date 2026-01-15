class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pq = []

        for i,j in points:
            dt = ((i*i) + (j*j)) ** 0.5
            heapq.heappush(pq, (-dt, [i,j]))

            if len(pq) > k:
                heapq.heappop(pq)
                

        res = []
        for p in pq:
            res.append(p[1])
        return res
