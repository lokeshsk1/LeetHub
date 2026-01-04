class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        res = 0

        for i in nums:
            div = 0
            tot = 0
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    one = j
                    two = i//j
                    if one != two:
                        tot += one + two
                        div += 2
                    else:
                        tot += one
                        div += 1
            if div == 4:
                res += tot
        
        return res
