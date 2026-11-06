class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        
        n = len(arr)
        res = 0

        dp = dict()

        for i in range(n):
            if arr[i] - difference in dp:
                dp[arr[i]] = 1 + dp[arr[i] - difference]
            else:
                dp[arr[i]] = 1

            res = max(res, dp[arr[i]])
        

        return res