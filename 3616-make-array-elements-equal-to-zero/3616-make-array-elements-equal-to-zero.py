class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        n = len(nums)
        left_sum = [0]*n
        right_sum = [0]*n

        tot = sum(nums)
        tot_till = 0

        for i in range(n):

            left_sum[i] = tot_till
            tot_till += nums[i]
            
            right_sum[i] = tot - tot_till

        print(left_sum, right_sum)

        res = 0
        for i in range(n):
            if nums[i] == 0:
                if abs(left_sum[i] - right_sum[i]) == 1:
                    res += 1
                elif left_sum[i] - right_sum[i] == 0:
                    res += 2

        return res
        