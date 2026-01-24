class Solution:
    # def fib(self, n: int) -> int:

    #     if n < 2:
    #         return n
        
    #     return self.fib(n-2) + self.fib(n-1)

    def fib(self, n: int) -> int:
        self.memo = [-1] * (n+1)
        return self.recurse(n)
    
    def recurse(self, n):

        if n < 2:
            return n
        
        if self.memo[n] != -1:
            return self.memo[n]
        
        self.memo[n] = self.recurse(n-2) + self.recurse(n-1)
        return self.memo[n]

        
        

