class Solution:
    def maxEnvelopes(self, envs: list[list[int]]) -> int:
        
        envs.sort(key = lambda x : (x[0], -x[1]))
        tails = []

        for x in envs:
            i = bisect_left(tails, x[1])

            if i == len(tails):
                tails.append(x[1])
            else:
                tails[i] = x[1]
        
        return len(tails)