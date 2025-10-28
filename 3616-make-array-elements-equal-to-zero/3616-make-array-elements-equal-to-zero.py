class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        n = len(nums)

        tot = sum(nums)
        tot_till = 0
        res = 0

        for i in range(n):

            left_sum = tot_till
            tot_till += nums[i]
            right_sum = tot - tot_till

            if nums[i] == 0:
                if abs(left_sum - right_sum) == 1:
                    res += 1
                elif left_sum - right_sum == 0:
                    res += 2            

        return res
        