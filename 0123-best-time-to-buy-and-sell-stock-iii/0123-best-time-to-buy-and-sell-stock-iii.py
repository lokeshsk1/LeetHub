class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)

        min_buy = prices[0]
        left = [0]*n
        right = [0]*n

        for i in range(1, len(prices)):

            min_buy = min(min_buy, prices[i])
            left[i] = max(left[i-1], prices[i] - min_buy)
        
        max_sell = prices[-1]

        for i in range(len(prices)-2, -1, -1):
            max_sell = max(max_sell, prices[i])
            right[i] = max(right[i+1], max_sell - prices[i])
        
        return max(left[i] + right[i] for i in range(n))



