class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        c = Counter(nums)

        pq = []

        for i in c:

            heapq.heappush(pq, (c[i], i))

            if len(pq) > k:
                heapq.heappop(pq)
        
        print(pq)
        return [e[1] for e in pq]