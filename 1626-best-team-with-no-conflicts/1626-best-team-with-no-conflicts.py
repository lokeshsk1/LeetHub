class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)

        # scores = [score for _, score in sorted(zip(ages, scores), reverse = 1) ]
        # ages = sorted(ages, reverse = 1)

        scores = [score for _, score in sorted(zip(ages, scores), reverse = 0) ]
        ages = sorted(ages, reverse = 0)

        dp = scores[:]
        res = 0

        # print(scores)

        for i in range(n):
            for j in range(i):
                if scores[j] <= scores[i]:
                    dp[i] = max(dp[i], dp[j] + scores[i])
            
            res = max(res, dp[i])

            # print(dp)

        return res
