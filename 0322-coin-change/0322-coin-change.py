class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
        
    #     dp = [amount+1]*(amount+1)
    #     dp[0] = 0

    #     print(dp)

    #     for i in range(1, amount+1):

    #         for c in coins:
    #             if i >= c:
    #                 dp[i] = min(1 + dp[i-c], dp[i])
        
    #     return -1 if dp[amount] == amount+1 else dp[amount]


        # [0, 1, 1, 2, 2, 1, 11, 11, 11, 11, 11, 11]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.amount = amount
        self.memo = [-1] * (amount+1)
        self.recurse(amount)
        print(self.memo)
        return self.memo[amount] if self.memo[amount] != amount+1 else -1

    def recurse(self, amount):

        if amount == 0:
            self.memo[amount] = 0
            return 0
        
        if self.memo[amount] != -1:
            return self.memo[amount]
        
        mini = self.amount + 1

        for c in self.coins:
            if amount - c >= 0:
                mini = min(mini, self.recurse(amount - c) + 1)
        
        self.memo[amount] = mini

        return mini