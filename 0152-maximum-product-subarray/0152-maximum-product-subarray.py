class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMax = currMin = res = nums[0]

        for i in range(1, len(nums)):
            tmp = currMax
            currMax = max(tmp*nums[i], nums[i], currMin*nums[i])
            currMin = min(tmp*nums[i], nums[i], currMin*nums[i])
            res = max(res, currMax)

        return res
