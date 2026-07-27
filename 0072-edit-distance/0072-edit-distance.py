class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        

        # #delete
        # dance
        # danc
        # ignore last char in s1 + 1

        # #replace
        # dancer
        # dancex
        # ignore last char in both + 1

        # #create
        # dance
        # dancer
        # ignore last char in s2 + 1


        n1 = len(s1); n2 = len(s2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(n2+1):
            dp[0][i] = i
        for j in range(n1+1):
            dp[j][0] = j

        print(dp)

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] != s2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        
        print(dp)

        return dp[-1][-1]

        # abc
        # xyz

        #        a b c
        #      0 1 2 3
        #   0. 0 1 2 3
        # x 1. 1 1 2 3
        # y 2. 2 2 2 3
        # z 3. 3 3 3 3


