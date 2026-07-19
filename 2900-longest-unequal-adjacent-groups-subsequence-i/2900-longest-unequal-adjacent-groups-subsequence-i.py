class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        # n = len(words)
        # dp = [0]*n

        # for i in range(n):
        #     for j in range(i):
        #         if groups[i] != groups[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        
        # print(dp)

        flag = groups[0]
        res = []

        for i,e in enumerate(groups):
            if e == flag:
                res.append(words[i])
                flag = 1 - flag

        return res
