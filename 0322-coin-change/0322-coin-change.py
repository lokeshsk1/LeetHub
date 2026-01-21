class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        print(dp)

        for i in range(1, amount+1):

            for c in coins:
                if i >= c:
                    dp[i] = min(1 + dp[i-c], dp[i])
        
        return -1 if dp[amount] == amount+1 else dp[amount]


        # [0, 1, 1, 2, 2, 1, 11, 11, 11, 11, 11, 11]