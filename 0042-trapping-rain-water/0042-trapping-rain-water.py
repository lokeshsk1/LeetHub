class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        n = len(height)

        rmax = [0]*n
        rmaxi = 0
        for i in range(n-1, -1, -1):
            rmaxi = max(rmaxi, height[i])
            rmax[i] = rmaxi

        lmax = 0
        for i in range(0, n):

            if height[i] < min(lmax, rmax[i]):
                res += min(lmax, rmax[i]) - height[i]

            lmax = max(lmax, height[i])

        

        return res
