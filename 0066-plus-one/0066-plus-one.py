class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        extra = 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9 and extra == 1:
                digits[i] = 0
                extra = 1
            else:
                digits[i] += extra
                extra = 0
        
        if extra == 1:
            return [1] + digits
            
        return digits
