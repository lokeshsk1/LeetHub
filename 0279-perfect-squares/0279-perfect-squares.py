class Solution:
    def numSquares(self, n: int) -> int:

        self.memo = [-1] * (n+1)
        return self.recurse(n)

    
    def recurse(self, n):

        if self.memo[n] != -1:
            return self.memo[n]

        if n < 4:
            self.memo[n] = n
            return n
        
        mini = n

        for i in range(1, int(n**0.5) + 1):
            mini = min(mini, 1 + self.recurse(n - (i*i)))
        
        self.memo[n] = mini
        return mini

