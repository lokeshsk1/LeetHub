class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 3 2 7 11
        # 3 2 3 11
        # 3 2 3 7
        # 3 2 3 3

        l = 1
        hi = max(piles)
        res = hi

        def can_complete(k):
            time = 0
            for i in piles:
                time += math.ceil(i/k)
            print(k, time, h)
            return time <= h
        
        while l <= hi:
            mid = (l+hi)//2
            if can_complete(mid):
                print(mid, l, hi)
                res = min(res, mid)
                hi = mid-1
            else:
                l = mid+1
        
        return res

