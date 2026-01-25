class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMax = currMin = res = nums[0]

        for i in range(1, len(nums)):
            tmp = currMax
            currMax = max(currMin*nums[i], tmp*nums[i], nums[i])
            currMin = min(currMin*nums[i], tmp*nums[i], nums[i])
            res = max(res, currMax)

        return res
