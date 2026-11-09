class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        
        n = len(days)
        dp = [0] * (n+1)

        for i in range(1, n+1):

            cost1 = costs[0] + dp[i-1]

            j = i-1
            while j > 0 and days[j-1] > days[i-1] - 7 :
                j -= 1
            cost7 = costs[1] + dp[j]

            j = i-1
            while j > 0 and days[j-1] > days[i-1] - 30:
                j -= 1
            cost30 = costs[2] + dp[j]

            # print(cost1, cost7, cost30)
            dp[i] = min(cost1, cost7, cost30)

        # print(dp)
        return dp[-1]