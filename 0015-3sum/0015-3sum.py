class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i in range(len(nums)-2):

            if i>0 and nums[i-1] == nums[i]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:

                tripSum = nums[i] + nums[left] + nums[right]

                if tripSum < 0:
                    left += 1
                elif tripSum > 0:
                    right -= 1
                else:
                    trip = [nums[i], nums[left], nums[right]]
                    res.append(trip)
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    left += 1
                    right -= 1

        return res
