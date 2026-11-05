class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [1] * n
        count = [1]*n

        maxLen = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        count[i] = count[j]
                    elif dp[i] == 1 + dp[j]:
                        count[i] += count[j]

            maxLen = max(maxLen, dp[i])
        
        print(maxLen, count)
        res = 0
        for i in range(n):
            if dp[i] == maxLen:
                res += count[i]                    
        
        return res

