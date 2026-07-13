class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        dp = [0]*(len(s))
        if s[0] != '0':
            dp[0] = 1

        if int(s[0] + s[1]) in range(10,27):
            dp[1] += 1

        if s[1] != '0':
            dp[1] += 1


        for i in range(2, len(s)):

            if int(s[i-1] + s[i]) in range(10,27):
                dp[i] += dp[i-2]

            print(dp, int(s[i-1] + s[i]) )

            if s[i] != '0':
                dp[i] += dp[i-1]
        
        return dp[-1]
            




# "226"

# B
# BB,  V
# BBF, VF, BZ