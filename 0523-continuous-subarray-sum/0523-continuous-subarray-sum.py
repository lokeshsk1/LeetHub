class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix_mod_hash = dict()
        tot = 0

        for i,e in enumerate(nums):
            tot += e

            if tot % k == 0 and i >= 1:
                return True
            if tot % k in prefix_mod_hash and i - prefix_mod_hash[tot % k] >= 2:
                return True

            if tot % k not in prefix_mod_hash:
                prefix_mod_hash[tot % k] = i
        
        return False