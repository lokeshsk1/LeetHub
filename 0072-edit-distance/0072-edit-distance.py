class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        
        n1 = len(s1); n2 = len(s2)

        dp = [ [n1]* (n2+1) for _ in range(n1+1)]

        for i in range(n1+1):
            for j in range(n2+1):
                if i==0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        print(dp)
        return dp[-1][-1]

        return 0