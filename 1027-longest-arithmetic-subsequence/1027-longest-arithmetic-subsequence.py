class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]


        res = 0

        for i in range(n):
            for j in range(i):

                diff = nums[i] - nums[j]
                dp[i][diff] = max(dp[i][diff] , 1 + dp[j][diff])
                res = max(res, dp[i][diff])
                

        return res+1
