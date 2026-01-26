class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxi = -1
        res = []

        for i in range(len(arr)-1, -1, -1):

            res.append(maxi)
            maxi = max(maxi, arr[i])
        
        return res[::-1]