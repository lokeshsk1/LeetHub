class Solution:
    def maxDepth(self, s: str) -> int:
        
        open = 0
        res = 0

        for i in s:
            if i == '(':
                open += 1
            elif i == ')':
                open -= 1
            res = max(res, open)
        
        return res