class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        pq = nums
        heapq.heapify(pq)
        
        while len(pq) > k:
            heapq.heappop(pq)

        self.pq = pq
        self.k = k
        
    def add(self, val: int) -> int:

        heapq.heappush(self.pq, val)

        if len(self.pq) > self.k:
            heapq.heappop(self.pq)

        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)