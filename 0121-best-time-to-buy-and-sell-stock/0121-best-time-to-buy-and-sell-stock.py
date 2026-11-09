class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        

        min_til = prices[0]
        res = 0

        for i in range(len(prices)):
            min_til = min(min_til, prices[i])
            res = max(res, prices[i] - min_til)
        
        return res