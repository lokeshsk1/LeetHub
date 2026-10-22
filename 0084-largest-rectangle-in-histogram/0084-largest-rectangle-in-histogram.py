class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # (start_index, height), heights strictly increasing
        best = 0

        for i, h in enumerate(heights + [0]):   # sentinel 0 flushes the stack at the end
            start = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx                      # new bar can extend back to where the popped bar began
            stack.append((start, h))

        return best