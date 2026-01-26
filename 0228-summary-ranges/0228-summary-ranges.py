class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []
        
        l = 0
        res = []

        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]+1:
                if nums[l] == nums[i-1]:
                    res.append(str(nums[l]))
                else:
                    res.append(str(nums[l]) + '->' + str(nums[i-1]))
                l = i

        if nums[l] == nums[-1]:
            res.append(str(nums[l]))
        else:
            res.append(str(nums[l]) + "->" + str(nums[-1]))

        return res


