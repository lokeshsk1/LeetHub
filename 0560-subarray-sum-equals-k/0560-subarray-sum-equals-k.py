class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix = 0
        dt = defaultdict(int)
        dt[0] = 1

        for i in nums:
            prefix += i
            
            if prefix - k in dt:
                res += dt[prefix - k]
            
            dt[prefix] = dt[prefix] + 1
            
        
        return res
            
        