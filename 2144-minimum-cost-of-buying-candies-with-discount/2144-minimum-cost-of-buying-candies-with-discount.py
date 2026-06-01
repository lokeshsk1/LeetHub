class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        if len(cost) < 3:
            return sum(cost)

        cost.sort(reverse = 0)
        tot = 0

        if len(cost) % 3 == 1:
            tot += cost[0]
        elif len(cost) % 3 == 2:
            tot += cost[0] + cost[1] 

        for i in range(len(cost)%3, len(cost)-2, 3):
            tot += cost[i+1] + cost[i+2]

        return tot