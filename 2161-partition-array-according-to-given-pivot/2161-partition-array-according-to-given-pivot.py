class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        n = len(nums)
        res = [pivot]*n
        left = 0
        right = n-1

        for i,j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):

            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                res[right] = nums[j]
                right -= 1
        
        # while left <= right:
        #     res[left] = pivot
        #     left += 1
        
        return res


