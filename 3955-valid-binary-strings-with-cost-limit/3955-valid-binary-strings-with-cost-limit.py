class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        def cost(n):
            cost = 0
            for i in range(len(n)):
                if n[i] == '1':
                    cost += i
            return cost

        res = []
        
        for i in range(0, 2**n):

            b = bin(i)[2:].zfill(n)
                        
            if (i & (i>>1)) ==0 and cost(b) <= k:
                res.append(b)

        return res


        
                