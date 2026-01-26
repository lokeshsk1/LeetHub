class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = ones = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, ones)
                ones = 0
            else:
                ones += 1
        
        return max(res, ones)