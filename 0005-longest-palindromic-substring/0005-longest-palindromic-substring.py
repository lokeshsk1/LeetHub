class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        if n == 1: return s

        dp = [[False] * n for _ in range(n)]

        for l in range(n):
            dp[l][l] = True

        res = s[0]

        for length in range(2, n+1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:

                    # print(i,j)

                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    
                    if dp[i][j] and length > len(res):
                        res = s[i:j+1]
                        # print(res)
        
        # for i in dp:
        #     print(i)

        return res