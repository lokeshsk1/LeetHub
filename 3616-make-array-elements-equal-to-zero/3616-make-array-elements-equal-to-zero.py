class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        n = len(nums)

        tot = sum(nums)
        left_sum = 0
        res = 0

        for i in range(n):

            left_sum += nums[i]
            right_sum = tot - left_sum

            if nums[i] == 0:
                if abs(left_sum - right_sum) == 1:
                    res += 1
                elif left_sum - right_sum == 0:
                    res += 2            

        return res
        