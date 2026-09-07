class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        a = (n * (n+1)) // 2
        b = sum(nums)
        return a - b
        # return sum([i for i in range(0,len(nums)+1)]) - sum(nums)