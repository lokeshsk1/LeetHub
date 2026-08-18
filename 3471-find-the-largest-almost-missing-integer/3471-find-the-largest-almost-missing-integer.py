class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        if len(nums) == k:
            return max(nums)

        ctr = Counter(nums)

        if k == 1:
            return max((c for c in ctr if ctr[c] == 1), default = -1)

        res = -1

        if ctr[nums[0]] == 1:
            res = nums[0]
        if ctr[nums[-1]] == 1:
            res = max(res, nums[-1])

        return res