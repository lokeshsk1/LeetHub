class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1
        curr = nums[0]

        for i in range(1, len(nums)):

            if nums[i] == curr:
                count += 1
            else:
                if count == 1:
                    curr = nums[i]
                else:
                    count -= 1
        
        return curr