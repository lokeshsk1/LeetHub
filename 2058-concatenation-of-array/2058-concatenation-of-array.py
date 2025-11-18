class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = []

        for _ in range(2):
            for i in nums:
                res.append(i)
            
        return res