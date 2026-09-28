class Solution:
    def canCross(self, stones: list[int]) -> bool:
        
        stst = set(stones)
        n = len(stones)

        dp = defaultdict(set)
        dp[1].add(1)

        for itr in range(1, n):
            
            stone = stones[itr]
            for j in dp[stone]:
                
                if j-1 > 0 and stone+j-1 in stst:
                    dp[stone + j-1].add(j-1)
                if stone+j in stst:
                    dp[stone +j].add(j)
                if stone+j+1 in stst:
                    dp[stone + j+1].add(j+1)
        
        # print(dp)

        return True if dp[stones[-1]] else False
