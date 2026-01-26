class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:

            mod = 0
            while num:
                mod += num%10
                num //= 10
                            
            num = mod
        
        return num