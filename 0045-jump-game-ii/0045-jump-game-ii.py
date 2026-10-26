class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_reach = 0
        mr = 0
        jumps = 0

        for i in range(len(nums)-1):
                        
            mr = max(mr, nums[i] + i)

            if i == max_reach:
                max_reach = mr
                jumps += 1

        return jumps
