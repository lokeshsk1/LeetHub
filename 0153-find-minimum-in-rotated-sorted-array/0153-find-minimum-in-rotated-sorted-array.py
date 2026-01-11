class Solution:
    def findMin(self, nums: List[int]) -> int:


        # a+10, a+11, a, a+1 a+2, a+3 , a+4, a+5, a+6, a+7, a+8, a+9

        #case 1:
        # l = a+10
        # mid = a+12
        # r = a+9

        # m > r , so we go right
        # for sure small is after mid

        # l = a+10
        # m = a+3
        # r = a+9

        # mid in left half - so r = m
        # omit sorted size, move towards un


        l = 0
        r = len(nums)-1
        res = float('inf')

        while l < r:

            m = (l+r)//2

            if nums[l] < nums[m] < nums[r]:
                break

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        return nums[l]

                    





