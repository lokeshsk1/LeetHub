class Solution:

    #Recursion
    # def fib(self, n: int) -> int:

    #     if n < 2:
    #         return n
        
    #     return self.fib(n-2) + self.fib(n-1)

    #Recursion + Memoization
    # def fib(self, n: int) -> int:
    #     self.memo = [-1] * (n+1)
    #     return self.recurse(n)
    
    # def recurse(self, n):

    #     if n < 2:
    #         return n
        
    #     if self.memo[n] != -1:
    #         return self.memo[n]
        
    #     self.memo[n] = self.recurse(n-2) + self.recurse(n-1)
    #     return self.memo[n]

    #DP
    # def fib(self, n: int) -> int:

    #     dp = [0,1]

    #     for i in range(2, n+1):
    #         dp.append(dp[i-2] + dp[i-1])
        
    #     return dp[n]

    #DP2
    def fib(self, n: int) -> int:

        p2 = 0; p1 = 1

        for i in range(n):
            p2, p1 = p1, p2+p1
        
        return p2



        
        

