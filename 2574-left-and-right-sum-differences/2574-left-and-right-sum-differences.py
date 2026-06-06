class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        rightSum = [0]

        for i in range(len(nums)-2, -1, -1):
            rightSum.append(rightSum[-1] + nums[i+1])
        rightSum.reverse()

        res = []
        leftSum = 0
        for i in range(len(nums)):
            print(leftSum, rightSum[i])
            res.append(abs(leftSum - rightSum[i]))
            leftSum += nums[i]            

        return res