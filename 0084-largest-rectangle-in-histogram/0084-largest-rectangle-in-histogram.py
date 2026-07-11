class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack[-1]
                stack.pop()
                curr = heights[top] * (i if stack==[] else (i-stack[-1]-1))
                res = max(res, curr)
            stack.append(i)
            
        while stack:
            top = stack[-1]
            stack.pop()
            curr = heights[top] * (n if stack==[] else (n-stack[-1]-1))
            res = max(res, curr)
            
        return res