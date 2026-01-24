class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        # a = cost[0] ; b = min(cost[0], cost[1])

        # for i in range(len(cost))

        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[-1], dp[-2]))
        
        print(dp)

        return min(dp[-1], dp[-2])

