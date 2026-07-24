class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)

        scores = [score for _, score in sorted(zip(ages, scores)) ]

        dp = scores[:]
        res = 0

        for i in range(n):
            for j in range(i):
                if scores[j] <= scores[i]:
                    dp[i] = max(dp[i], dp[j] + scores[i])
            
            res = max(res, dp[i])

        return res
