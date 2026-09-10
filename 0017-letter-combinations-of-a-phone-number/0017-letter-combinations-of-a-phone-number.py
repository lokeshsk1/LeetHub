class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in phone[int(next_digits[0])]:
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        return res