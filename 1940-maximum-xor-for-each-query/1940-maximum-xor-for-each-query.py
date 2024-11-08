class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        res = []
        maxXOR = (2**maximumBit)-1
        cumXOR = 0

        for i in nums:
            cumXOR ^= i
            k = maxXOR - cumXOR
            # print(cumXOR, k)
            res.append(k)
        
        return res[::-1]

