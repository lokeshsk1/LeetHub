class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]*len(nums)
        right = [1]*len(nums)
        res = [1]*len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[-i-1] = right[-i] * nums[-i]

            res[i] *= left[i]
            res[-i-1] *= right[-i-1]

        return res