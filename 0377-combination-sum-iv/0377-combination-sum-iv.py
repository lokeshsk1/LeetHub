class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
    
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for j in nums:
                if j <= i:
                    dp[i] += dp[i-j]
        
        print(dp)
        return dp[target]


        # dp[1] = 0 = 1
        # dp[2] = 0, 1 = 1 + 1 = 2
        # dp[3] = 0, 1, 2 = 1 + 1 + 2 = 4
        # dp[4] = 1, 2, 3 = 1 + 2 + 4 = 7 
