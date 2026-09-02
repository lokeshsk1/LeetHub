class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        min_pq = []
        max_pq = []

        for i in range(len(weights)-1):

            pairSum = weights[i] + weights[i+1]

            heapq.heappush(min_pq, pairSum)
            heapq.heappush(max_pq, -pairSum)

        min_score = max_score = 0
        
        for _ in range(k-1):
            min_score += heapq.heappop(min_pq)
            max_score -= heapq.heappop(max_pq)
        
        return max_score - min_score
        

