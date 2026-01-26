class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        kad = self.kadanes(arr)

        if k == 1:
            return kad
            
        tot = sum(arr)
        sufMax = self.suffixSumMax(arr)
        preMax = self.prefixSumMax(arr)

        case1 = kad
        case2 = sufMax + preMax + ((k-2)*tot if tot > 0 else 0)

        return max(case1, case2) % ((10**9)+7)

        
    def kadanes(self, arr):

        currSum = maxSum = 0

        for i in arr:
            currSum = max(i, currSum + i)
            maxSum = max(maxSum, currSum)
        
        return maxSum

    def prefixSumMax(self, arr):

        res = pre = 0

        for i in arr:
            pre += i
            res = max(res, pre)
        
        return res
    
    def suffixSumMax(self, arr):

        res = suf = 0
        
        for i in arr[::-1]:
            suf += i
            res = max(res, suf)
        
        return res

