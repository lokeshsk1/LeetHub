class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        posSum = self.kadanes(nums)

        print(posSum)

        if posSum < 0:
            return posSum
        
        tot = sum(nums)

        nums = [-i for i in nums]
        negSum = self.kadanes(nums)

        return max(posSum, tot + negSum)
        

    def kadanes(self, nums):

        currSum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum+nums[i], nums[i])
            res = max(res, currSum)
        
        return res