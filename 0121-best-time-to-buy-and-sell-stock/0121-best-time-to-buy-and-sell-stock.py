class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_till = prices[0]
        res = 0

        for i in prices:
            min_till = min(min_till, i)
            res = max(res, i - min_till)
        
        return res
