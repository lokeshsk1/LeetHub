class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        length = [1]*len(nums)
        count = [1]*len(nums)

        res = 0
        maxLen = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:

                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

                maxLen = max(maxLen, length[i])
        
        
        for i in range(len(nums)):
            if length[i] == maxLen:
                res += count[i]

        print(length, end = "\n")
        print(count)

        return res

