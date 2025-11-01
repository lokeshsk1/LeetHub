class Solution:
    def countStableSubarrays(self, nums: List[int]) -> int:

        res = 0
        hmap = defaultdict(lambda : defaultdict(int))
        psum = [0]*len(nums)
        psum[0] = nums[0]

        for i in range(1, len(nums)):
            psum[i] = psum[i-1] + nums[i]

        for i in range(1, len(nums)):
            
            n = nums[i]
            target = psum[i] - 2*n
            
            res += hmap[n][target]

            hmap[nums[i-1]][psum[i-1]] += 1

        return res