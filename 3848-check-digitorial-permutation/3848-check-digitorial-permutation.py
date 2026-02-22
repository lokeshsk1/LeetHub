class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        factSum = sum(math.factorial(int(i)) for i in str(n))
        return Counter(str(factSum)) == Counter(str(n))