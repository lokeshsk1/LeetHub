class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        tails = []
        res = 0

        for x in nums:
            i = bisect_left(tails, x)

            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        
        return len(tails)