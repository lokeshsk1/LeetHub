class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        res = 0
        
        for i in range(len(nums)):
            dist = set()
            even = 0
            odd = 0
            for j in range(i, len(nums)):
                if nums[j] not in dist:
                    if nums[j] % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                
                dist.add(nums[j])

                if even == odd:
                    res = max(res, j-i+1)
            
        return res
                
