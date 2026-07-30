class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l,m = 0,0

        for i in nums:
            if i == 0:
                l += 1
                m += 1
            elif i == 1:
                m += 1
        
        # print(l,m)

        nums[:l] = [0]*l
        nums[l:m] = [1]*(m-l)
        nums[m:] = [2]*(len(nums)-m)

        return nums