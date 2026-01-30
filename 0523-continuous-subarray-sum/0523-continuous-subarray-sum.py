class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        hmap = dict()
        hmap[0] = -1
        preSum = 0

        # 2 9 11 15
        # 2 11 22 37
        # 2 4 1 2

        for i in range(len(nums)):
            preSum = (preSum + nums[i]) % k

            if preSum not in hmap:
                hmap[preSum] = i
            elif i - hmap[preSum] >= 2:
                return True

        return False
            
        
            

