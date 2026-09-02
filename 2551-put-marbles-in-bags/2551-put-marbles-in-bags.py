class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        min_pq = []
        max_pq = []

        for i in range(len(weights)-1):

            pairSum = weights[i] + weights[i+1]

            print(pairSum)
            heapq.heappush(min_pq, pairSum)
            heapq.heappush(max_pq, -pairSum)

        min_score = weights[0] + weights[-1]
        max_score = weights[0] + weights[-1]
        
        print(min_pq)

        for _ in range(k-1):
            mini = heapq.heappop(min_pq)
            maxi = heapq.heappop(max_pq)
            min_score += mini
            max_score -= maxi
        
        print(min_score, max_score)

        return max_score - min_score
        

