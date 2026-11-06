class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: list[int]) -> list[int]:
        
        n = len(nums)

        tails = []
        res = []
        
        for x in nums:

            i = bisect_right(tails, x)

            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
            
            res.append(i+1)

            # print(tails)
        
        return res