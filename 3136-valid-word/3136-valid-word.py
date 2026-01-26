class Solution:
    def isValid(self, word: str) -> bool:
        
        chars = 0
        vow = 0
        cons = 0

        for i in word:

            if not i.isalnum():
                return False
            
            if i.isalpha():
                if i in 'aeiouAEIOU':
                    vow += 1
                else:
                    cons += 1
        
        return len(word) >= 3 and vow > 0 and cons > 0
        
