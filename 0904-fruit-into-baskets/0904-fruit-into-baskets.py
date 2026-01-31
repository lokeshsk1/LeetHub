class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        
        num1 = -1
        num2 = -1
        countNum2 = 0
        res = currMax = 0

        for i in range(len(nums)):

            if nums[i] == num1 or nums[i] == num2:
                currMax += 1
            else:
                currMax = countNum2 + 1
            
            if nums[i] == num2:
                countNum2 += 1
            else:
                countNum2 = 1
                num1, num2 = num2, nums[i]
                
            res = max(res, currMax)
        
        return res
        

