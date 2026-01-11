class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, e in enumerate(nums):

            if i>0 and nums[i-1] == nums[i]:
                continue

            target = -e

            hmap = {}

            for j in range(i+1, len(nums)):
                if target - nums[j] in hmap:
                    l = [ nums[i], nums[hmap[target-nums[j]]], nums[j] ]
                    res.append(sorted(l))
                hmap[nums[j]] = j
        
        
        return list(set(map(tuple, res)))