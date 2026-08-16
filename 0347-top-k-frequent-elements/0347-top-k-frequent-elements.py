class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        size = k
        c = Counter(nums)

        pq = []

        for k,v in c.items():

            heapq.heappush(pq, (v, k))

            if len(pq) == size+1:
                heapq.heappop(pq)
        
        res = [j for i,j in pq]
        return res


