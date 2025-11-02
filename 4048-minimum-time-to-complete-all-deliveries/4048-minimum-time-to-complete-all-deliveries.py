class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:

        low = d[0] + d[1]
        high = 4*low
        res = high

        lcm = (r[0]*r[1]) // math.gcd(r[0],r[1])

        def can_complete(time):

            a_slots = time - (time // r[0])
            b_slots = time - (time // r[1])
            ab_slots = time - (time // lcm)
            return a_slots >= d[0] and b_slots >= d[1] and ab_slots >= (d[0]+d[1])

        while low <= high:

            mid = low + (high - low) // 2

            if can_complete(mid):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
    
        return res  




    
        
