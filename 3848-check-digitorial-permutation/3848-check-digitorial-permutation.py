class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        factSum = 0
        for i in str(n):
            factSum += math.factorial(int(i))

        return Counter(str(factSum)) == Counter(str(n))