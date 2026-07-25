class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()

        n = len(nums)

        dp = [[nums[i]] for i in range(n)]
        res = [nums[0]]

        for i in range(1, len(nums)):
            for j in range(i):
                curr = [nums[i]]
                for k in dp[j]:
                    if nums[i] % k == 0 or k % nums[i] == 0:
                        curr.append(k)
                    
                if len(curr) > len(dp[i]):
                    dp[i] = curr
                    
            if len(dp[i]) > len(res):
                res = dp[i]
            
            # print(dp)

        return res
