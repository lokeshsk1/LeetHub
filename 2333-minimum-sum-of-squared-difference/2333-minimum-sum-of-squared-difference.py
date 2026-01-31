class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        pq = []

        for i in range(len(nums1)):
            heapq.heappush(pq, abs(nums1[i] - nums2[i])*-1)
        
        tot = -sum(pq)
        k = k1+k2

        if tot <= k:
            return 0

        while k > 0:
            curr = -heappop(pq)
            step = math.ceil(k / len(nums1))
            curr -= step
            k -= step
            heappush(pq, -curr)
        
        return sum(i*i for i in pq)

        
