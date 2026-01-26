class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        temp = x
        rev = 0

        while x:
            curr = x % 10
            rev = rev*10 + curr
            x //= 10
        
        return rev == temp

