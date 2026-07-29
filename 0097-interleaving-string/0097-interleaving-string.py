class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        r = len(s1)
        c = len(s2)
        
        if r+c != len(s3):
            return False

        dp = [[0]*(c+1) for _ in range(r+1)]
        dp[0][0] = 1

        for i in range(1, r+1):
            if s1[i-1] == s3[i-1] and dp[i-1][0] == 1:
                dp[i][0] = 1

        for j in range(1, c+1):
            if s2[j-1] == s3[j-1] and dp[0][j-1] == 1:
                dp[0][j] = 1

        print(dp)

        for i in range(1, r+1):
            for j in range(1, c+1):
                case1 = s1[i-1] == s3[i+j-1] and dp[i-1][j]
                case2 = s2[j-1] == s3[i+j-1] and dp[i][j-1]
                if case1 or case2:
                    dp[i][j] = 1

        for row in dp:
            print(row, end = '\n')

        return dp[-1][-1]













        # ab
        # cd

        # acdb - a + cdb | b , cd
        # cdb - b + d | b, d
        # bd - d | d
        # d - d

        # abc | ax

        # axabc
